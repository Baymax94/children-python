//We always have to include the library
#include "LedControl.h"

/*
 Now we need a LedControl to work with.
 ***** These pin numbers will probably not work with your hardware *****
 pin 12 is connected to the DataIn 
 pin 11 is connected to the CLK 
 pin 10 is connected to LOAD 
 We have only a single MAX72XX.
 */
LedControl lc=LedControl(12,11,10,1);
int state[64];
int light[64];
void setup() {
  // put your setup code here, to run once:
    /*
   The MAX72XX is in power-saving mode on startup,
   we have to do a wakeup call
   */
  lc.shutdown(0,false);
  /* Set the brightness to a medium values */
  lc.setIntensity(0,8);
  /* and clear the display */
  lc.clearDisplay(0);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0)
  {
    for(int i=0;i<64;i++)
    {
      state[i]=Serial.parseInt();
      light[i]=Serial.parseInt();
      delay(2);
      }
     for(int j=0;j<64;j++)
     {
      lc.setLed(0,(light[j]-1)/8,(light[j]-1)%8,state[j]);
      }
    }

}
