/****************************************************************
Main CPP for RedBot wheel encoder.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

21 Jan 2014- Mike Hord, SparkFun Electronics

Code developed in Arduino 1.0.5, on an SparkFun Redbot v12.
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

RedBotEncoder *encoderObject=0; // Create a local pointer to an instance of this
                                //  class, so we can edit the counts with other
                                //  library functions.

RedBotEncoder::RedBotEncoder(int lPin, int rPin)
{
  // RedBot only breaks out ten valid pins:
  //  A0-A5 a.k.a. D14-19 (PCINT 8-13)
  //  D3 (PCINT 19)
  //  D9-D11 (PCINT 1-3)
  // We'll need a whopping case statement to set up the pin change interrupts
  //  for this; in fact, we'll need two, but I'll abstract it to a function.
  //  A call to setPinChangeInterrupt() enables pin change interrupts for that
  //  pin, and pin change interrupts for the group that pin is a part of.
  pinMode(lPin, INPUT_PULLUP);
  pinMode(rPin, INPUT_PULLUP);
  setPinChangeInterrupt(lPin, LENCODER);
  setPinChangeInterrupt(rPin, RENCODER);
  lCounts = 0;
  rCounts = 0;
  encoderObject = this; // We want a local pointer to the class member that is
                        //  instantiated in the sketch, so we can manipulate its
                        //  private members with other classes.
  lDir = 1;		// default direction to forward -- used for encoder counting
  rDir = 1;		// default direction to forward -- used for encoder counting
}

// This private function changes the counter when a tick happens. The direction
//  is set by the functions that set the motor direction.
void RedBotEncoder::wheelTick(WHEEL wheel)
{
  switch(wheel)
  {
    case LEFT:
      lCounts+= (long)lDir;
      break;
    case RIGHT:
      rCounts+= (long)rDir;
      break;
    case BOTH:
      break;
  }
}

// Public function to clear the encoder counts.
void RedBotEncoder::clearEnc(WHEEL wheel)
{
  switch(wheel)
  {
    case LEFT:
      lCounts = 0;
      break;
    case RIGHT:
      rCounts = 0;
      break;
    case BOTH:
      lCounts = 0;
      rCounts = 0;
      break;
  }
}

// Public function to read the encoder counts for a given wheel.
long RedBotEncoder::getTicks(WHEEL wheel)
{
  switch(wheel)
  {
    case LEFT:
      return lCounts;
    case RIGHT:
      return rCounts;
    case BOTH:
      return 0;
  }
  return 0;
}