/****************************************************************
Main CPP for RedBot accelerometer board.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

21 Jan 2014- Mike Hord, SparkFun Electronics

Code developed in Arduino 1.0.5, on an SparkFun Redbot v12.
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

RedBotAccel::RedBotAccel()
{  
  byte buffer[2];
  // This sets the bit rate of the bus; I want 100kHz. See the
  //  datasheet for details on how I came up with this value.
  TWBR = 72;
  
  // The very first thing we want to do is reset the accelerometer. Since
  //  we don't know what's happened since the last time we powered the
  //  thing up, the best we can do is reset it by twiddling the reset bit
  //  (bit 6) in CTRL2 register (0x2B).
  buffer[0] = 0x40;
  xlWriteBytes(0x2B, buffer, 1);
  
  // Accelerometer configuration- there are five registers (starting with
  //  0x2A) that must be configured for the accelerometer to operate. We'll
  //  create a byte buffer and fill it with the values we need, then push it
  //  to the accelerometer. Only the first two registers need to be fiddled
  //  with, the rest are for interrupts and things we don't need to worry
  //  about.
  
  // Let's set the dynamic range to max out at 8g instead of 2.
  buffer[0] = 0x02;
  xlWriteBytes(0x0E, buffer, 1);
  
  // Now we'll populate our buffer.
  // CTRL1 register, five settings here:
  //  7:6 - sample rate during sleep mode (leave default 50Hz)
  //  5:3 - data rate (leave default 800Hz)
  //  2   - low noise mode (set to 1 to activate)
  //  1   - 8-bit mode (leave 0 to disable)
  //  0   - active/standby (leave 0, for now)
  buffer[0] = 0x04;
  
  // CTRL2 register, five more settings:
  //  7   - self-test (leave 0, disabled)
  //  6   - software reset (leave 0, no reset)
  //  5   - no use
  //  4:3 - sleep mode (leave 00, normal mode)
  //  2   - sleep enable (leave 0, disable auto sleep)
  //  1:0 - active mode (set 10, hi-res oversample)
  buffer[1] = 0x02;
  
  // Now that we've populated our buffer, we can push it to the accelerometer.
  xlWriteBytes(0x2A, buffer, 2);
  
  // Now that we've set that up, we can enable the part by writing 0x05 to
  //  CTRL1.
  buffer[0] = 0x05;
  xlWriteBytes(0x2A, buffer, 1);
}

// read() initiates a capture of the current x, y, and z values, and stores
//  them in the appropriate class member variables.
void RedBotAccel::read()
{
  // The first step, the easy step, is to grab the values. We'll put 'em in
  //  a byte buffer.
  byte buffer[6];
  xlReadBytes(0x01, buffer, 6);

  // Next, we need to copy the data into the member variables so they can be
  //  accessed by the user.
  x = buffer[0]<<8 | buffer[1];
  y = buffer[2]<<8 | buffer[3];
  z = buffer[4]<<8 | buffer[5];
  
  // Adding these three calculations adds ~ 700us to this process.
  // This method takes ~856 us to run w/o them in and about 1532 us with 
  // these floating point operations. (BH)
  angleXZ = 180*atan2(x,z)/PI;
  angleXY = 180*atan2(x,y)/PI;
  angleYZ = 180*atan2(y,z)/PI;
  
}

// For bump detection, we're looking for a transient in the Z direction. The
// bump should be pretty hard, so hopefully, we'll be able to distinguish
// between a bump and a tap.
void RedBotAccel::enableBump()
{
  byte buffer[8];
  
  // The *very* first thing we need to do is disable the chip; otherwise,
  //  we can't change the register settings.
  xlReadBytes(0x2A, buffer, 1);
  buffer[0] &= 0xFE;
  xlWriteBytes(0x2A, buffer, 1);

  // To enable tap detection, we need to write some data to registers
  // 0x21-0x28. See Freescale app note 4072 for more info about setting
  // this up.
  
  // The very first thing we'll do is enable the LPF for pulse detection.
  // This is in register 0x0F.
  buffer[0] = 0x10;
  xlWriteBytes(0x0F, buffer, 1);
  
  // Since tap detection and bump detection use the same system resources,
  // we need to fetch the data from the accelerometer before we can set up
  // tap.
  xlReadBytes(0x21, buffer, 8);
  
  // Now that we have the current settings, we can turn on z-axis tap detection
  // by fiddling with the appropriate bits.
  
  // 0x21 (PULSE_CFG)- We need to set bit 6 (ELE, latch events into register)
  // and bit 0 (XSPEFE, x-axis single pulse event function enable)
  buffer[0] = 0x41;
  
  // 0x22 (PULSE_SRC)- we'll read this to check for pulses; it's read only, so
  // we don't need to do anything with it here.
  buffer[1] |= 0x00; // just a placeholder
  
  // 0x23- X pulse threshold- experimentally determined to be a good value for a
  // threshold.
  buffer[2] = 32;
  // 0x24- Y pulse threshold
  // Both of these can be ignored, and shouldn't be touched, in case they're
  // configured for something else.
  buffer[3] |= 0x00; // placeholder
  
  // 0x25 (PULSE_THSZ)
  buffer[4] |= 0;
  
  // 0x26 (PULSE_TMLT)- maximum length a pulse must be to be detected as a tap.
  // The length is dependent upon three things: the sampling rate (800Hz),
  // whether Pulse_LPF is set or clear in register 0x0F (it's not), and the
  // sampling mode (Hi-res). Charts on pp34-35 of the datasheet tell us that
  // the maximum pulse length here is this register value times 0.625ms.
  buffer[5] = 25;  // maximum pulse length of 62.5ms
  
  // 0x27 (PULSE_LTCY)- lockout time after a pulse occurs before another one
  // will be sensed. Charts for value are on page 35 of the datasheet.
  buffer[6] = 50; // 125ms lockout period
  
  // 0x28 (PULSE_WIND)- window within which a second tap must occur to register
  // a double tap event. We aren't worried about double taps (yet), so let's
  // leave this unchanged.
  buffer[7] |= 0x00;  // placeholder
  
  // Write the values we just set up back into the accelerometer.
  xlWriteBytes(0x21, buffer, 8);
  
  // Now we need to put the device back into active mode.
  xlReadBytes(0x2A, buffer, 1);
  buffer[0] |= 0x01;
  xlWriteBytes(0x2A, buffer, 1);
}

boolean RedBotAccel::checkBump()
{
  byte buffer = 0;
  xlReadBytes(0x22, &buffer, 1);   // check the PULSE_SRC register to see if a
                                   //  pulse event has been registered. This
                                   //  will clear all pulse events
  if ((buffer&0x10)!=0)   return true;  // Mask for X events.
  else               return false;
  
}

void RedBotAccel::setBumpThresh(int xThresh)
{  
  byte buffer;
  // The *very* first thing we need to do is disable the chip; otherwise,
  //  we can't change the register settings.
  xlReadBytes(0x2A, &buffer, 1);
  buffer &= 0xFE;
  xlWriteBytes(0x2A, &buffer, 1);
  
  // 0x23- X pulse threshold- experimentally determined to be a good value for a
  //  threshold.
  buffer = (byte)xThresh;  
  
  // Write the value we just set up back into the accelerometer.
  xlWriteBytes(0x23, &buffer, 1);
  
  // Now we need to put the device back into active mode.
  xlReadBytes(0x2A, &buffer, 1);
  buffer |= 0x01;
  xlWriteBytes(0x2A, &buffer, 1);
}

// Private function that reads some number of bytes from the accelerometer.
void RedBotAccel::xlReadBytes(byte addr, byte *buffer, byte len)
{  
  unsigned int timeout = 0; // We're going to use this to set a timeout on the 
                            //  amount of time we'll wait for the bus to become
                            //  available. The minimum period here is about 4ms
                            //  on a 16MHz device.
  
  // First, we need to write the address we want to read from, so issue a write
  //  with that address. That's two steps: first, the slave address:
  TWCR = START_COND;          // Send a start condition         
  while (!(TWCR&(1<<TWINT))) // When TWINT is set, start is complete, and we
                              //  can initiate data transfer.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  TWDR = XL_ADDR<<1;          // Load the slave address
  TWCR = CLEAR_TWINT;         // Clear TWINT to begin transmission (I know,
                              //  it LOOKS like I'm setting it, but this is
                              //  how we clear that bit. Dumb.)
  while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  // Now, we need to send the address we want to read from:
  TWDR = addr;                // Load the slave address
  TWCR = CLEAR_TWINT;        // Clear TWINT to begin transmission (I know,
                              //  it LOOKS like I'm setting it, but this is
                              //  how we clear that bit. Dumb.)
  while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  TWCR = STOP_COND;
  
  timeout = 0;
  
  // Now, we issue a repeated start (by doing what we just did again), and this
  //  time, we set the READ bit as well.
  TWCR = START_COND;          // Send a start condition
  while (!(TWCR&(1<<TWINT)))  // When TWINT is set, start is complete, and we
                              //  can initiate data transfer.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  TWDR = (XL_ADDR<<1) | I2C_READ;  // Load the slave address and set the read bit
  TWCR = CLEAR_TWINT;        // Clear TWINT to begin transmission (I know,
                              //  it LOOKS like I'm setting it, but this is
                              //  how we clear that bit. Dumb.)
  while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  
  // Now, we can fetch data from the slave by clearing TWINT, waiting, and
  //  reading the data. Rinse, repeat, as often as needed.
  for (byte i = 0; i < len; i++)
  {
    if (i == len-1) TWCR = CLEAR_TWINT; // Clear TWINT to begin transmission (I know,
                                //  it LOOKS like I'm setting it, but this is
                                //  how we clear that bit. Dumb.)
    else TWCR = NEXT_BYTE;
    while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
    buffer[i] = TWDR;           // Now our data can be fetched from TWDR.
  }
  // Now that we're done reading our data, we can transmit a stop condition.
  TWCR = STOP_COND;
}

void RedBotAccel::xlWriteBytes(byte addr, byte *buffer, byte len)
{
  unsigned int timeout = 0; // We're going to use this to set a timeout on the 
                            //  amount of time we'll wait for the bus to become
                            //  available. The minimum period here is about 4ms
                            //  on a 16MHz device.
                            
  // First, we need to write the address we want to read from, so issue a write
  //  with that address. That's two steps: first, the slave address:
  TWCR = START_COND;          // Send a start condition         
  while (!(TWCR&(1<<TWINT))) // When TWINT is set, start is complete, and we
                              //  can initiate data transfer.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  TWDR = XL_ADDR<<1;          // Load the slave address
  TWCR = CLEAR_TWINT;         // Clear TWINT to begin transmission (I know,
                              //  it LOOKS like I'm setting it, but this is
                              //  how we clear that bit. Dumb.)
  while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  // Now, we need to send the address we want to read from:
  TWDR = addr;                // Load the slave address
  TWCR |= CLEAR_TWINT;         // Clear TWINT to begin transmission (I know,
                              //  it LOOKS like I'm setting it, but this is
                              //  how we clear that bit. Dumb.)
  while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  
  // Now, we can send data to the slave by putting data into TWDR, clearing
  //  TWINT, and waiting for TWINT. Rinse, repeat, as often as needed.
  for (byte i = 0; i < len; i++)
  {
    TWDR = buffer[i];           // Now our data can be sent to TWDR.
    TWCR |= CLEAR_TWINT;        // Clear TWINT to begin transmission (I know,
                                //  it LOOKS like I'm setting it, but this is
                                //  how we clear that bit. Dumb.)
    while (!(TWCR&(1<<TWINT)))  // Wait for TWINT again.
  {
    if (++timeout == 0) return; // time out if the bus is busy. In most cases,
  }                           //  "busy" means no sensor on the bus.
  timeout = 0;
  }
  // Now that we're done writing our data, we can transmit a stop condition.
  TWCR = STOP_COND;
}
