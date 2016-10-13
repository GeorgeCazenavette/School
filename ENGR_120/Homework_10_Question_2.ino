#include <Servo.h>
Servo servo;
void makeSound(int pin, float freq){
  digitalWrite(pin,HIGH);
  delayMicroseconds(int(1/freq/2*100000));
  digitalWrite(pin,LOW);
  delayMicroseconds(int(1/freq/2*100000));}
void setup() {
  // put your setup code here, to run once:
  //pinMode(2,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(6,INPUT);
  Serial.begin(9600);
  servo.attach(2);} 
void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(analogRead(4));
  if (analogRead(4)>700)  {
    servo.writeMicroseconds(1700);}
  else{
    servo.writeMicroseconds(1300);}
  if (digitalRead(6)==HIGH){
    for(float i=333;i<=1500;i=i+.5){
      makeSound(10,i);}
    for(float i=333;i<=1200;i=i+.5){
      makeSound(10,i);}
    for(float i=1200;i>=333;i=i-.5){
      makeSound(10,i);}}}
