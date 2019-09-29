/***********************************************************************
 * Exp8_2_WindUp -- RedBot Experiment 8.2
 * 
 * This is a fun demo of using the accelerometer to "wind up" the the redBot
 * As you tilt the Redbot forward, it should speed up. When you place it flat
 * it will race forward for 3 seconds and then stop.
 *
 * Hardware setup:
 * You'll need to attach the RedBot Accelerometer board to hader on the upper
 * right side of the mainboard. See the manual for details on how to do this.
 * 
 * This sketch was written by SparkFun Electronics, with lots of help from 
 * the Arduino community. This code is completely free for any use.
 * 
 * 8 Oct 2013 M. Hord
 * Revised, 31 Oct 2014 B. Huang 
 * 
 * 8 Oct 2013 M. Hord
 * 
 * This experiment was inspired by Paul Kassebaum at Mathworks, who made
 * one of the very first non-SparkFun demo projects and brought it to the
 * 2013 Open Hardware Summit in Boston. Thanks Paul!
 ***********************************************************************/

#include <RedBot.h>
RedBotMotors motors;
int motorPower;  // variable for setting the drive power

// The RedBot library includes support for the accelerometer. We've tried
// to make using the accelerometer as easy as to use as possible.

RedBotAccel accelerometer;

void setup(void)
{
  Serial.begin(9600);
}

void loop(void)
{
  accelerometer.read(); // updates the x, y, and z axis readings on the accelerometer

  int xAccel = accelerometer.x;
  int yAccel = accelerometer.y;
  int zAccel = accelerometer.z;

  float XZ = accelerometer.angleXZ;  // read in the XZ angle
  float YZ = accelerometer.angleYZ;  // read in the YZ angle
  float XY = accelerometer.angleXY;  // read in the XY angle

  Serial.print(XZ, 2);  // prints out floating point number with 2 decimal places
  Serial.print("\t");   // tab
  Serial.println(motorPower);  // prints out motorPower

    // if the angle is greater than 20 degrees
  if (XZ > 20)  
  { 
    // while the angle is greater than 20, speed up or down (match the speed to the angle)
    while(XZ > 15)  // 5 degree buffer
    {
      motorPower = map(XZ, 0, 90, 0, 255);
      motors.drive(motorPower);   // Adjust the motor power with the scaled
      //  value from the accelerometer.
      accelerometer.read();       // Update the readings, so the while() loop
      XZ = accelerometer.angleXZ; // Update the variable for the XZ angle    

      // debug print statements
      Serial.print(XZ, 2);  // prints out XZ angle with 2 decimal places
      Serial.print("\t");   // tab
      Serial.println(motorPower);  // prints out motorPower
      delay(200);  // give you a chance to set the robot down
    }
  }
  // If our accelerometer reading is less than 1500, we just want to let
  //  the motor run, but slow it down a little bit at a time.
  else
  {
    motors.drive(motorPower);
    delay(200);     // We don't want to slow the motor too fast, so while
    //  we're slowing the motor, let's put in a delay so we don't blow through loop() quite as fast.
    if (motorPower > 50) 
    {
      motorPower = motorPower - 1;  // reduce motorSpeed by 1 each time -- until it is less than 50, then just stop.
    }
    else
    {
      motorPower = 0;
    }
  }  
}


