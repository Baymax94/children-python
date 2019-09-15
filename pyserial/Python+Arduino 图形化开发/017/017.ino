#define RED 9
#define GREEN 10
#define BLUE 11
int r,g,b;
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
  r=Serial.parseInt();
  g=Serial.parseInt();
  b=Serial.parseInt();
  color_led(r,g,b);
  
  }

}

void color_led(int r,int g,int b)
{
  set_led(RED,r);
  set_led(RED,g);
  set_led(RED,b);
}

void set_led(int pin,int val)
{
  if(val)
  {
    digitalWrite(pin,LOW);
  }
  else
  {
    digitalWrite(pin,HIGH);
    }
}

