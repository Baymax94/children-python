/***********************************************************************
 * Exp3_Turning -- RedBot Experiment 3
 * 
 * Explore turning with the RedBot by controlling the Right and Left motors
 * separately.
 * 
 * Hardware setup:
 * This code requires only the most basic setup: the motors must be
 * connected, and the board must be receiving power from the battery pack.
 * 
 * 23 Sept 2013 N. Seidle/M. Hord
 * 04 Oct 2014 B. Huang
 ***********************************************************************/
#include <RedBot.h>  // This line "includes" the library into your sketch.

RedBotMotors motors; // Instantiate the motor control object.

void setup()
{
  // drive forward -- instead of using motors.drive(); Here is another way.
  motors.rightMotor(150); // Turn on right motor clockwise medium power (motorPower = 150) 
  motors.leftMotor(-150); // Turn on left motor counter clockwise medium power (motorPower = 150) 
  delay(1000);       // for 1000 ms.
  motors.brake();    // brake() motors

  // pivot -- spinning both motors CCW causes the RedBot to turn to the right
  motors.rightMotor(-100); // Turn CCW at motorPower of 100
  motors.leftMotor(-100);  // Turn CCW at motorPower of 100
  delay(500);        // for 500 ms.    
  motors.brake();    // brake() motors
  delay(500);        // for 500 ms.    

  // drive forward -- instead of using motors.drive(); Here is another way.
  motors.rightMotor(150); // Turn on right motor clockwise medium power (motorPower = 150) 
  motors.leftMotor(-150); // Turn on left motor counter clockwise medium power (motorPower = 150)
  delay(1000);       // for 1000 ms.
  motors.brake();     // brake() motors
}

void loop()
{
  // Figure 8 pattern -- Turn Right, Turn Left, Repeat
  //  motors.leftMotor(-200);  // Left motor CCW at 200
  //  motors.rightMotor(80);   // Right motor CW at 80
  //  delay(2000);
  //  motors.leftMotor(-80);    // Left motor CCW at 80
  //  motors.rightMotor(200);   // Right motor CW at 200
  //  delay(2000); 
}


