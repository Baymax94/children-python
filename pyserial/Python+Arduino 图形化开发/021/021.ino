#define RED 9
#define GREEN 10
#define BLUE 11
int color;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(RED,OUTPUT);
  pinMode(GREEN,OUTPUT);
  pinMode(BLUE,OUTPUT);
  digitalWrite(RED,HIGH);
  digitalWrite(BLUE,HIGH);
  digitalWrite(GREEN,HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:
  while(!Serial){}
  if(Serial.available()>0)
  {
  color=Serial.parseInt();
  color_led(color);
  
  }

}

void color_led(int c)
{
  switch(c)
  {
    case 1:
    digitalWrite(RED,LOW);
    digitalWrite(BLUE,HIGH);
    digitalWrite(GREEN,HIGH);
    break;
    case 2:
    digitalWrite(RED,HIGH);
    digitalWrite(BLUE,HIGH);
    digitalWrite(GREEN,LOW);
    break;
    case 3:
    digitalWrite(RED,HIGH);
    digitalWrite(BLUE,LOW);
    digitalWrite(GREEN,HIGH);
    break;
    }
  
}
