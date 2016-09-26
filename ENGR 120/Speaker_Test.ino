 void makeSound(int pin, float freq)
{
  digitalWrite(pin,HIGH);
  delayMicroseconds(int(1/freq/2*100000));
  digitalWrite(pin,LOW);
  delayMicroseconds(int(1/freq/2*100000));
}

void makeSound(int pin, float freq, float dur)
{
  for(float t=1; t<=dur/(1/freq);t++)
  {
    digitalWrite(pin,HIGH);
    delayMicroseconds(int(1/freq/2*100000));
    digitalWrite(pin,LOW);
    delayMicroseconds(int(1/freq/2*100000));
  }
}
void setup() {
  pinMode(10,OUTPUT);
  pinMode(6,INPUT);
}

void loop() {
  if(digitalRead(6)==HIGH)
  {
    for(float i=333;i<=1500;i=i+.5)
    {
      makeSound(10,i);
    }
    for(float i=333;i<=1200;i=i+.5)
    {
      makeSound(10,i);
    }
    for(float i=1200;i>=333;i=i-.5)
    {
      makeSound(10,i);
    }
  }
  if(digitalRead(7)==HIGH)
  {
    makeSound(10,333,5);
  }

}
