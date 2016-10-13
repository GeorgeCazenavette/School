#include <Servo.h>

Servo leftWheel;
Servo rightWheel;

void forward(float percent, float seconds)
{
  leftWheel.writeMicroseconds(-percent*200+1500);
  rightWheel.writeMicroseconds(percent*200+1500);
  delay(int(1000*seconds));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void forward()
{
   leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1700);
}

void rightTurn(float seconds)
{
  leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1300);
  delay(int(1000*seconds));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void leftTurn(float seconds)
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1700);
  delay(int(1000*seconds));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}
void reverse()
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1300);
}

void reverse(float percent, float seconds)
{
  leftWheel.writeMicroseconds(percent*200+1500);
  rightWheel.writeMicroseconds(-percent*200+1500);
  delay(int(1000*seconds));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}
void stopMove()
{
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}
void setup() {
  // put your setup code here, to run once:
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(7,INPUT);
  pinMode(6,INPUT);
  leftWheel.attach(4);
  rightWheel.attach(3);
}

void loop() {
  // put your main code here, to run repeatedly:
  forward();
  if(digitalRead(7)==HIGH)
  { 
    reverse(.5,1);
    rightTurn(.5);
  }
  if(digitalRead(6)==HIGH)
  {
    reverse(.5,1);
    leftTurn(.5);
  }
}
