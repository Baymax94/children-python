/****************************************************************
Main CPP for RedBot button control.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

04 Oct 2014- B. Huang, SparkFun Electronics

Code developed in Arduino 1.0.6, on an SparkFun Redbot rev02
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

#define BUTTON_PIN 12

// Constructor. Mostly for pin setup; note that it's not necessary to configure
//  PWM pins as they will be automatically configured with the analogWrite()
//  function is called.
RedBotButton::RedBotButton()
{
  // Sets the "default" state of the button to be HIGH. 
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  }

boolean RedBotButton::read()
{
  return(!digitalRead(BUTTON_PIN));
}