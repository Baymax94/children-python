/***********************************************************************
 * Exp7_1_RotaryEncoder -- RedBot Experiment 7
 * 
 * Knowing where your robot is can be very important. The RedBot supports
 * the use of an encoder to track the number of revolutions each wheels has
 * made, so you can tell not only how far each wheel has traveled but how
 * fast the wheels are turning.
 * 
 * This sketch was written by SparkFun Electronics, with lots of help from 
 * the Arduino community. This code is completely free for any use.
 * 
 * 8 Oct 2013 M. Hord
 * Revised, 31 Oct 2014 B. Huang 
 ***********************************************************************/

#include <RedBot.h>
RedBotMotors motors;

RedBotEncoder encoder = RedBotEncoder(A2, 10);  // initializes encoder on pins A2 and 10
int buttonPin = 12;
int countsPerRev = 192;   // 4 pairs of N-S x 48:1 gearbox = 192 ticks per wheel rev

// variables used to store the left and right encoder counts.
int lCount;
int rCount;

void setup()
{
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("left    right");
  Serial.println("================");
}

void loop(void)
{
  // wait for a button press to start driving.
  if (digitalRead(buttonPin) == LOW)
  {
    encoder.clearEnc(BOTH);  // Reset the counters.
    motors.drive(150);        // Start driving forward.
  }

  // store the encoder counts to a variable.
  lCount = encoder.getTicks(LEFT);    // read the left motor encoder
  rCount = encoder.getTicks(RIGHT);   // read the right motor encoder

  // print out to Serial Monitor the left and right encoder counts.
  Serial.print(lCount);
  Serial.print("\t");
  Serial.println(rCount);

  // if either left or right motor are more than 5 revolutions, stop
  if ((lCount >= 5*countsPerRev) || (rCount >= 5*countsPerRev) )
  {
    motors.brake();
  }
}

