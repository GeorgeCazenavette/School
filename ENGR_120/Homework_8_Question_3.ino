void setup() {
  // put your setup code here, to run once:
  pinMode(3,OUTPUT);
  pinMode(6,INPUT);
  pinMode(7,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(7)==HIGH && digitalRead(6)==LOW)
  {
    digitalWrite(3,HIGH);
    delayMicroseconds(1300);
    digitalWrite(3,LOW);
    delay(20);
  }
  if(digitalRead(6)==HIGH && digitalRead(7)==LOW)
  {
    digitalWrite(3,HIGH);
    delayMicroseconds(1700);
    digitalWrite(3,LOW);
    delay(20);
  }
}
