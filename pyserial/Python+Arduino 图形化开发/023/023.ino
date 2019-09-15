#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11  //DHT11
DHT dht(DHTPIN,DHTTYPE);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial){}
  int h=dht.readHumidity();
  // Read temperature as Celsius (the default)
  int t=dht.readTemperature();
  // Check if any reads failed and exit early (to try again)
  if (isnan(h)||isnan(t)){
    return;
    }
   Serial.print(h);
   Serial.print(",");
   Serial.println(t);
   delay(2000);

}
