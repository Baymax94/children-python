/***********************************************************************
 * Exp7_2_DriveDistance -- RedBot Experiment 7.2
 * 
 * In an earlier experiment, we used a combination of speed and time to
 * drive a certain distance. Using the encoders, we can me much more accurate.
 * In this example, we will show you how to setup your robot to drive a certain
 * distance regardless of the motorPower.
 * 
 * This sketch was written by SparkFun Electronics, with lots of help from 
 * the Arduino community. This code is completely free for any use.
 * 
 * 8 Oct 2013 M. Hord
 * Revised, 31 Oct 2014 B. Huang 
 ***********************************************************************/
#include <RedBot.h>

RedBotMotors motors;

RedBotEncoder encoder = RedBotEncoder(A2, 10);
int buttonPin = 12;
int countsPerRev = 192;   // 4 pairs of N-S x 48:1 gearbox = 192 ticks per wheel rev

float wheelDiam = 2.56;  // diam = 65mm / 25.4 mm/in
float wheelCirc = PI*wheelDiam;  // Redbot wheel circumference = pi*D

void setup()
{
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop(void)
{
  // drive on button press.
  if (digitalRead(buttonPin) == LOW)
  {
    driveDistance(12, 150);  // drive 12 inches, at motorPower = 150.
  }
}

void driveDistance(float distance, int motorPower)
{
  long lCount = 0;
  long rCount = 0;
  float numRev;
  // debug
  Serial.print("driveDistance() ");
  Serial.print(distance);
  Serial.print(" inches at ");
  Serial.print(motorPower);
  Serial.println(" power.");

  numRev = (float) distance / wheelCirc;
  Serial.println(numRev, 3);
  encoder.clearEnc(BOTH);  // clear the encoder count
  motors.drive(motorPower);

  while (rCount < numRev*countsPerRev)
  {
    // while the left encoder is less than the target count -- debug print 
    // the encoder values and wait -- this is a holding loop.
    lCount = encoder.getTicks(LEFT);
    rCount = encoder.getTicks(RIGHT);
    Serial.print(lCount);
    Serial.print("\t");
    Serial.print(rCount);
    Serial.print("\t");
    Serial.println(numRev*countsPerRev);
  }
  // now apply "brakes" to stop the motors.
  motors.brake();
}

