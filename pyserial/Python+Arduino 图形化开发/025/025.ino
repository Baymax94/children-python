int val;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  digitalWrite(13,HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()>0)
  {
    val=Serial.parseInt();
    if(val==1)
    {
      digitalWrite(13,HIGH);
      }
    else if(val==0)
    {
      digitalWrite(13,LOW);
      }
    }

}
