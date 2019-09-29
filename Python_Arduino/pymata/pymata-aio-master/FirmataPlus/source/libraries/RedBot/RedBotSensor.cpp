/****************************************************************
Main CPP for RedBot IR reflectance sensors.

This code is beerware; if you use it, please buy me (or any other
SparkFun employee) a cold beverage next time you run into one of
us at the local.

21 Jan 2014- Mike Hord, SparkFun Electronics

Code developed in Arduino 1.0.5, on an SparkFun Redbot v12.
****************************************************************/

#include "RedBot.h"
#include <Arduino.h>

RedBotSensor::RedBotSensor(int pin)
{
  _pin = pin;
  _BGLevel = -1;
  _detectLevel = -1;
}

int RedBotSensor::read()
{
  return analogRead(_pin);
}

// If both the background and detection levels for this sensor have been
//  set, returns true.
boolean RedBotSensor::calStatus()
{
  if (_BGLevel != -1 && _detectLevel != -1) return true;
  else                                      return false;
}

// An attempt at a decent single-call, quick return line detection function.
boolean RedBotSensor::check()
{
  // Collect a sample.
  int level = analogRead(_pin);
  
  // Are we looking for something that is darker than our normal level (say,
  //  a table edge, or a black stripe on a white surface) or something that
  //  is brighter than our normal level (say, a piece of copper tape? on a
  //  dark floor)?
  // Remember, the darker the surface, the higher the value returned.
  if (_BGLevel < _detectLevel) // Light-on-dark situation
  {
    // For a light-on-dark detection, we're looking to see if the level is
    //  higher than _BGLevel. Our threshold will be a rise above the BGLevel
    //  of 1/4 the difference between background and detect levels.
    int threshold = (_detectLevel - _BGLevel)>>2;
    if (level-threshold > _BGLevel) return true;
    else                            return false;
  }
  else // Dark-on-light situation
  {
    // For a dark-on-light detection, we'll do exactly the opposite: check to
    //  see if the level is lower than _BGLevel by at least 1/4 the difference
    //  between the levels.
    int threshold = (_BGLevel - _detectLevel)>>2;
    if (level+threshold < _BGLevel) return true;
    else                            return false;
  }
}

// setBGLevel() is used to calibrate the level that we expect to see when we
//  aren't seeing something interesting. 
int RedBotSensor::setBGLevel()
{
  _BGLevel = analogRead(_pin);

  return _BGLevel;
}

// setDetectLevel() works exactly the same as setBGLevel(), but with different
//  variables. 
int RedBotSensor::setDetectLevel()
{
  _detectLevel = analogRead(_pin);

  return _detectLevel;
}