/***********************************************************************
 * Exp8_1_AccelerometerRead -- RedBot Experiment 8.1
 * 
 * Measuring speed, velocity, and acceleration are all key
 * components to robotics. This first experiment will introduce
 * you to using the Accelerometer sensor on the RedBot.
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

// The RedBot library includes support for the accelerometer. We've tried
// to make using the accelerometer as easy as to use as possible.

RedBotAccel accelerometer;

void setup(void)
{
  Serial.begin(9600);
}

void loop(void)
{
  accelerometer.read(); // updates the x, y, and z axis readings on the acceleromter

  // Display out the X, Y, and Z - axis "acceleration" measurements and also
  // the relative angle between the X-Z, Y-Z, and X-Y vectors. (These give us 
  // the orientation of the RedBot in 3D space. 

  Serial.print("("); 
  Serial.print(accelerometer.x);
  Serial.print(", ");  // tab

  Serial.print(accelerometer.y);
  Serial.print(", ");  // tab

  Serial.print(accelerometer.z);
  Serial.print(") -- ");  // tab

  Serial.print("[");
  Serial.print(accelerometer.angleXZ);
  Serial.print(", "); 
  Serial.print(accelerometer.angleYZ);
  Serial.print(", "); 
  Serial.print(accelerometer.angleXY);
  Serial.println("]");

  // short delay in between readings/
  delay(100); 
}

