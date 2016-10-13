#include <Servo.h> 

Servo myservo;

void setup() 
{ 
  myservo.attach(2);
  myservo.write(180);
} 

void loop() {} 

