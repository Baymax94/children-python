float checkdistance_7_8() {
  digitalWrite(7, LOW);
  delayMicroseconds(2);
  digitalWrite(7, HIGH);
  delayMicroseconds(10);
  digitalWrite(7, LOW);
  float distance = pulseIn(8, HIGH) / 58.00;
  delay(10);
  return distance;
}

void setup(){
  pinMode(7, OUTPUT);
  pinMode(8, INPUT);
  Serial.begin(9600);
}

void loop(){
  Serial.println(checkdistance_7_8());
  delay(1000);

}
