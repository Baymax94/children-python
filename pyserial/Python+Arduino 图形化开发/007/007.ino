#define LED 13
int state;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial){}
  if(Serial.available()>0)
  {
  state=Serial.parseInt();
  digitalWrite(LED,state);
  }

}
