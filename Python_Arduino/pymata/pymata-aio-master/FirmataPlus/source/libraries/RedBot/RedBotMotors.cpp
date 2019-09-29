/****************************************************************
Main CPP for RedBot motor control.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

21 Jan 2014- Mike Hord, SparkFun Electronics

Code developed in Arduino 1.0.5, on an SparkFun Redbot v12.
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

extern RedBotEncoder *encoderObject;   // Declared in RedBotEncoder.cpp

// Constructor. Mostly for pin setup; note that it's not necessary to configure
//  PWM pins as they will be automatically configured with the analogWrite()
//  function is called.
RedBotMotors::RedBotMotors()
{
  // The interface to the motor driver is kind of ugly. It's three pins per
  //  channel: two that define role (forward, reverse, stop, brake) and one
  //  PWM input for speed.
  pinMode(R_CTRL_1, OUTPUT);
  pinMode(R_CTRL_2, OUTPUT);
  pinMode(L_CTRL_1, OUTPUT);
  pinMode(L_CTRL_2, OUTPUT);
}

// stop() allows the motors to coast to a stop, rather than trying to stop them
//  quickly. As will be the case with functions affecting both motors, the
//  global stop just calls the individual stop functions for each wheel.
void RedBotMotors::stop()
{
  leftStop();
  rightStop(); 
}

// coast() is the same as stop() -- but more descriptive of what this method does.
// it allows the motors to coast to a stop, rather than trying to stop them
// quickly. As will be the case with functions affecting both motors, the
// global stop just calls the individual stop functions for each wheel. This is
//  exactly the same as the stop() method. stop() is retained for backwards compatibilty
void RedBotMotors::coast()
{
  leftStop();
  rightStop(); 
}


// brake() effectively shorts the two leads of the motor together, which causes
//  the motor to resist being turned. It stops quite quickly. 
void RedBotMotors::brake()
{
  leftBrake();
  rightBrake(); 
}

// drive() starts both motors. It figures out whether the motors should go
//  forward or revers, then calls the appropriate individual functions. Note
//  the use of a 16-bit integer for the speed input; an 8-bit integer doesn't
//  have the range to reach full speed. The calls to the actual drive functions
//  are only 8-bit, since we only have 8-bit PWM.
void RedBotMotors::drive(int speed)
{
  if (speed > 0)
  {
    leftFwd((byte)(abs(speed)));
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    leftRev((byte)(abs(speed)));
    rightRev((byte)(abs(speed)));
  }
}

void RedBotMotors::drive(int speed, int duration)
{ // this variant of drive() integrates a delay duration to allow for single commmand instruction.
  if (speed > 0)
  {
    leftFwd((byte)(abs(speed)));
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    leftRev((byte)(abs(speed)));
    rightRev((byte)(abs(speed)));
  }
  delay(duration);
  leftStop();
  rightStop(); 
}


// pivot() is very much like drive(), except the motors are driven in opposite
//  directions, so as to pivot the motor on it's central axis. Positive numbers
//  turn / rotate the robot clockwise (to the right) -- assuming the motors are hooked up properly.
void RedBotMotors::pivot(int speed)
{
  if (speed > 0)
  {
    leftFwd((byte)(abs(speed)));
    rightRev((byte)(abs(speed)));
  }
  else
  {
    leftRev((byte)(abs(speed)));
    rightFwd((byte)(abs(speed)));
  }
}

void RedBotMotors::pivot(int speed, int duration)
{
  if (speed > 0)
  {
    leftRev((byte)(abs(speed)));
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    leftFwd((byte)(abs(speed)));
    rightRev((byte)(abs(speed)));
  }
  delay(duration);
  leftStop();
  rightStop(); 
  
}

// Basically the same as drive, but omitting the left motor.
void RedBotMotors::rightMotor(int speed)
{
  if (speed > 0)
  {
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    rightRev((byte)(abs(speed)));
  }
}

void RedBotMotors::rightMotor(int speed, int duration)
{
  if (speed > 0)
  {
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    rightRev((byte)(abs(speed)));
  }
  delay(duration);
  rightStop(); 
}

// Basically the same as drive(), but omitting the right motor.
void RedBotMotors::leftMotor(int speed)
{
  if (speed > 0)
  {
    leftRev((byte)(abs(speed)));
  }
  else
  {
    leftFwd((byte)(abs(speed)));
  }
}

void RedBotMotors::leftMotor(int speed, int duration)
{
  if (speed > 0)
  {
    leftRev((byte)(abs(speed)));
  }
  else
  {
    leftFwd((byte)(abs(speed)));
  }
  delay(duration);
  leftStop();
}

void RedBotMotors::rightDrive(int speed)
{
  if (speed > 0)
  {
    rightFwd((byte)(abs(speed)));
  }
  else
  {
    rightRev((byte)(abs(speed)));
  }
}void RedBotMotors::leftDrive(int speed)
{
  if (speed > 0)
  {
    leftFwd((byte)(abs(speed)));
  }
  else
  {
    leftRev((byte)(abs(speed)));
  }
}


// From here out, we deal with the nitty gritty details of telling the motor
//  driver what to do. For more information about this, refer to the TB6612FNG
//  datasheet.
void RedBotMotors::leftBrake()
{
  digitalWrite(L_CTRL_1, HIGH);
  digitalWrite(L_CTRL_2, HIGH);
  analogWrite(PWM_L, 0);
}

void RedBotMotors::rightBrake()
{
  digitalWrite(R_CTRL_1, HIGH);
  digitalWrite(R_CTRL_2, HIGH);
  analogWrite(PWM_R, 0);
}

void RedBotMotors::leftStop() // allows left motor to coast to a stop
{
  digitalWrite(L_CTRL_1, LOW);
  digitalWrite(L_CTRL_2, LOW);
  analogWrite(PWM_L, 0);
}

void RedBotMotors::rightStop() // allows right motor to coast to a stop
{
  digitalWrite(R_CTRL_1, LOW);
  digitalWrite(R_CTRL_2, LOW);
  analogWrite(PWM_R, 0);
}

void RedBotMotors::leftCoast()  // same as rightStop()
{
  digitalWrite(L_CTRL_1, LOW);
  digitalWrite(L_CTRL_2, LOW);
  analogWrite(PWM_L, 0);
}

void RedBotMotors::rightCoast()  // same as leftStop()
{
  digitalWrite(R_CTRL_1, LOW);
  digitalWrite(R_CTRL_2, LOW);
  analogWrite(PWM_R, 0);
}


/******************************************************************************
Private functions for RedBotMotor
******************************************************************************/
// These are the motor-driver level abstractions for turning a given motor the
//  right direction. Users never see them, and *should* never see them, so we
//  make them private.

void RedBotMotors::leftFwd(byte spd)
{
  digitalWrite(L_CTRL_1, HIGH);
  digitalWrite(L_CTRL_2, LOW);
  analogWrite(PWM_L, spd);
  // If we have an encoder in the system, we want to make sure that it counts
  //  in the right direction when ticks occur.
  if (encoderObject != 0)
  {
    encoderObject->lDir = 1;
  }
}

void RedBotMotors::leftRev(byte spd)
{
  digitalWrite(L_CTRL_1, LOW);
  digitalWrite(L_CTRL_2, HIGH);
  analogWrite(PWM_L, spd);
  // If we have an encoder in the system, we want to make sure that it counts
  //  in the right direction when ticks occur.
  if (encoderObject != 0)
  {
    encoderObject->lDir = -1;
  }
}

void RedBotMotors::rightFwd(byte spd)
{
  digitalWrite(R_CTRL_1, HIGH);
  digitalWrite(R_CTRL_2, LOW);
  analogWrite(PWM_R, spd);
  // If we have an encoder in the system, we want to make sure that it counts
  //  in the right direction when ticks occur.
  if (encoderObject != 0)
  {
    encoderObject->rDir = 1;
  }
}

void RedBotMotors::rightRev(byte spd)
{
  digitalWrite(R_CTRL_1, LOW);
  digitalWrite(R_CTRL_2, HIGH);
  analogWrite(PWM_R, spd);
  // If we have an encoder in the system, we want to make sure that it counts
  //  in the right direction when ticks occur.
  if (encoderObject != 0)
  {
    encoderObject->rDir = -1;
  }
}
