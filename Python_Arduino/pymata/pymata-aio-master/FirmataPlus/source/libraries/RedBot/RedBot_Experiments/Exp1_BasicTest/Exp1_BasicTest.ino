/***********************************************************************
 * Exp1_BasicTest -- RedBot Experiment 1
 * 
 * Time to make sure the electronics work! To test everything out, we're
 * going to blink the LED on the board. 
 * 
 * This sketch was written by SparkFun Electronics, with lots of help from 
 * the Arduino community.
 * 
 * 23 Sept 2013 N. Seidle/M. Hord
 * 04 Oct 2014 B. Huang
 ***********************************************************************/

// setup() function runs once at the very beginning.
void setup()
{
  pinMode(13, OUTPUT); // The RedBot has an LED connected to pin 13. 
  // Pins are all generic, so we have to first configure it 
  // as an OUTPUT using this command.
}

// loop() function repeats over and over... forever!
void loop()
{
  // Blink sequence
  digitalWrite(13, HIGH); // Turns LED ON -- HIGH puts 5V on pin 13. 
  delay(500);             // delay(500) "pauses" the program for 500 milliseconds
  digitalWrite(13, LOW);  // Turns LED OFF -- LOW puts 0V on pin 13.
  delay(500);             // delay(500) "pauses" the program for 500 milliseconds
  // The total delay period is 1000 ms, or 1 second.
}

/***********************************************************************
 * In Arduino, an LED is often connected to pin 13 for "debug" purposes. 
 * This LED is used as an indicator to make sure that we're able to upload
 * code to the board. It's also a good indicator that your program is running.
 **********************************************************************/


