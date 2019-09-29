/***********************************************************************
 * Exp5_Bumpers -- RedBot Experiment 5
 * 
 * Now let's experiment with the whisker bumpers. These super-simple switches
 * let you detect a collision before it really happens- the whisker will
 * bump something before your robot crashes into it.
 * 
 * This sketch was written by SparkFun Electronics, with lots of help from 
 * the Arduino community.
 * This code is completely free for any use.
 * Visit https://learn.sparkfun.com/tutorials/redbot-inventors-kit-guide 
 * for SIK information.
 * 
 * 8 Oct 2013 M. Hord
 * Revised 30 Oct 2014 B. Huang
 ***********************************************************************/

#include <RedBot.h>
RedBotMotors motors;

RedBotBumper lBumper = RedBotBumper(3);  // initialzes bumper object on pin 3
RedBotBumper rBumper = RedBotBumper(11); // initialzes bumper object on pin 11

int buttonPin = 12; // variable to store the button Pin 

int lBumperState;  // state variable to store the bumper value
int rBumperState;  // state variable to store the bumper value

void setup()
{
  // nothing here.
}

void loop()
{
  motors.drive(255);
  lBumperState = lBumper.read();  // default INPUT state is HIGH, it is LOW when bumped
  rBumperState = rBumper.read();  // default INPUT state is HIGH, it is LOW when bumped

    if (lBumperState == LOW) // left side is bumped/
  { 
    reverse();    // backs up
    turnRight();  // turns
  }

  if (rBumperState == LOW) // right side is bumped/
  { 
    reverse();   // backs up
    turnLeft();  // turns
  }

}

// reverse() function -- backs up at full power
void reverse()
{
  motors.drive(-255);
  delay(500);
  motors.brake();
  delay(100);  // short delay to let robot fully stop
}

// turnRight() function -- turns RedBot to the Right
void turnRight()
{
  motors.leftMotor(-150);  // spin CCW
  motors.rightMotor(-150); // spin CCW
  delay(500);
  motors.brake();
  delay(100);  // short delay to let robot fully stop
}

// turnRight() function -- turns RedBot to the Left
void turnLeft()
{
  motors.leftMotor(+150);  // spin CW
  motors.rightMotor(+150); // spin CW
  delay(500);
  motors.brake();
  delay(100);  // short delay to let robot fully stop
}


