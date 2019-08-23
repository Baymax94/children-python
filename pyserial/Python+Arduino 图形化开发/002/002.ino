//int val;
int a=1;
int b=2;
int c=3;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  /*while(Serial.available()>0)
  {
    val=Serial.parseInt();
    Serial.println(val);
  }
  */
  while(!Serial){}
  Serial.print(a);
  Serial.print(",");
  Serial.print(b);
  Serial.print(",");
  Serial.print(c);
  Serial.print("\n");
  delay(500);
  a++;
  b++;
  c++;
}
