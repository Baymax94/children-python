/****************************************************************
Main CPP for RedBot whisker bumper.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

21 Jan 2014- Mike Hord, SparkFun Electronics

Code developed in Arduino 1.0.5, on an SparkFun Redbot v12.
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

void (*whiskerAction[10])(void); // Pointer to an array of functions
                                 //  describing what should happen if a
                                 //  given pin has a whisker event.
                                 
// Standard class constructor, assumes that you want to halt the motors on a
//  bump. A more skilled programmer than I could figure out the error message
//  I get if I try to use the brake() function that's a part of the RedBotMotor
//  class; I worked around it by making a globally available one.
RedBotBumper::RedBotBumper(int pin)
{
//  setPinChangeInterrupt(pin, WHISKER);
  pinMode(pin, INPUT_PULLUP);
  //setBumpFunction(pin, &brake);
  _pin = pin;  // set local variable for the pin
  }

// Bonus points constructor, which allows the user to connect a custom function
//  to a bumper.
RedBotBumper::RedBotBumper(int pin, void(*functionPointer)(void))
{
  setPinChangeInterrupt(pin, WHISKER);
  pinMode(pin, INPUT_PULLUP);
  setBumpFunction(pin, functionPointer);
  _pin = pin;  // set local variable for the pin
}

boolean RedBotBumper::read()
{
  return(digitalRead(_pin));
}
// Non-class function that puts the brakes on. This is the default behavior if
//  the user doesn't specify a custom function for the bumper trigger.
void brake(void)
{
  digitalWrite(L_CTRL_1, HIGH);
  digitalWrite(L_CTRL_2, HIGH);
  analogWrite(PWM_L, 0);
  digitalWrite(R_CTRL_1, HIGH);
  digitalWrite(R_CTRL_2, HIGH);
  analogWrite(PWM_R, 0);
}

// I elected to create a function just to do this, rather than trying to wrap
//  it into the setPinChangeInterrupt() function. When a bumper action occurs,
//  a function will be called. By default, it's to brake the motors; users can
//  write a function of their own and this function will point the interrupt
//  at that custom function instead.
void RedBotBumper::setBumpFunction(int pin, void(*functionPointer)(void))
{
  switch(pin)
  {
    case A0:
      whiskerAction[PCINT_A0] = functionPointer;
      break;
    case A1:
      whiskerAction[PCINT_A1] = functionPointer;
      break;
    case A2:
      whiskerAction[PCINT_A2] = functionPointer;
      break;
    case A3:
      whiskerAction[PCINT_A3] = functionPointer;
      break;
    case A4:
      whiskerAction[PCINT_A4] = functionPointer;
      break;
    case A5:   
      whiskerAction[PCINT_A5] = functionPointer; 
      break;
    case 3:     
      whiskerAction[PCINT_3] = functionPointer;
      break;    
    case 9:     
      whiskerAction[PCINT_9] = functionPointer;
      break; 
    case 10: 
      whiskerAction[PCINT_10] = functionPointer;
      break; 
    case 11:
      whiskerAction[PCINT_11] = functionPointer;
      break;
  }
}