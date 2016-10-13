#include <Servo.h>

int arg = 1540;

Servo servo;
void setup() {
  // put your setup code here, to run once:
  servo.attach(2);
  servo.writeMicroseconds(arg);
  delay(3500);
  servo.writeMicroseconds(1500);
}

void loop() {
  // put your main code here, to run repeatedly:
 
}
