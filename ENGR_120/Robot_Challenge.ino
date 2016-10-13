//George Cazenavette Robot Challenge
//HNRS 120 H05

#include <Servo.h>

Servo leftWheel;
Servo rightWheel;
Servo spinner;

void driveForward()
{
  leftWheel.detach();
  rightWheel.detach();
  leftWheel.attach(4);
  rightWheel.attach(3);
}

void driveReverse()
{
  leftWheel.detach();
  rightWheel.detach();
  leftWheel.attach(3);
  rightWheel.attach(4);
}
void forward(float sec)
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1300);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void forward()
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1300);
}

void reverse(float sec)
{
  leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1700);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void reverse()
{
  leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1700);
}

void openClamp()
{
  spinner.writeMicroseconds(1400);
  delay(1000);
  spinner.writeMicroseconds(1500);
}

void closeClamp()
{
  spinner.writeMicroseconds(1600);
  delay(1000);
  spinner.writeMicroseconds(1500);
}

void turnRight(float sec)
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1700);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void turnRight()
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1700);
}

void turnLeft(float sec)
{
  leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1300);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void turnLeft()
{
  leftWheel.writeMicroseconds(1300);
  rightWheel.writeMicroseconds(1300);
}

void rightForward(float sec)
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1465);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void rightForward()
{
  leftWheel.writeMicroseconds(1700);
  rightWheel.writeMicroseconds(1465);
}

void slowRight()
{
  leftWheel.writeMicroseconds(1600);
  rightWheel.writeMicroseconds(1500);
}

void leftForward(float sec)
{
  leftWheel.writeMicroseconds(1535);
  rightWheel.writeMicroseconds(1300);
  delay(int(sec*1000));
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void leftForward()
{
  leftWheel.writeMicroseconds(1535);
  rightWheel.writeMicroseconds(1300);
}

void slowLeft()
{
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1400);
}
void halt()
{
  leftWheel.writeMicroseconds(1500);
  rightWheel.writeMicroseconds(1500);
}

void nano()//nanosystems mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  delay(200);
  turnRight(.25);
  delay(50);
  forward(1.5);
  delay(50);
  turnRight(.3);
  delay(50);
  forward(.4);
  delay(50);
  reverse(.5);
  delay(50);
  turnLeft(.3);
  delay(50);
  reverse(2);
  delay(50);
  turnLeft(.25);
  
}

void chemical()//chemical mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  delay(200);
  forward(1.5);
  delay(50);
  closeClamp();
  delay(50);
  reverse(1.6);
  delay(50);
  openClamp();
}

void civil()//civil mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  delay(200);
  turnLeft(.4);
  delay(50);
  forward(1.3);
  delay(50);
  reverse(1.8);
  delay(50);
}
void bio()//biomedical mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  delay(200);
  leftWheel.detach();
  rightWheel.detach();
  leftWheel.attach(3);
  rightWheel.attach(4);
  closeClamp();
  delay(50);
  leftForward(2.5);
  forward(2.5);
  delay(50);
  turnRight(.5);
  delay(50);
  reverse(.6);
  delay(50);
  openClamp();
  delay(50);
  forward(.6);
  delay(50);  
}

void mech()//mechanical mission
{
  driveForward();
  turnRight(.3);
  delay(50);
  forward(2);
  delay(50);
  turnLeft(.5);
  delay(50);
  forward(1);
  closeClamp();
  delay(50);
  driveReverse();
  forward(1);
  delay(50);
  turnRight(.5);
  delay(50);
  forward(1.8);
  rightForward(2);
  forward(3);
  delay(50);
  turnRight(.3);
  delay(50);
  forward(1);
  openClamp();
}

void electrical()//electrical mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  delay(200);
  leftWheel.detach();
  rightWheel.detach();
  leftWheel.attach(3);
  rightWheel.attach(4);
  closeClamp();
  delay(50);
  leftForward(2.5);
  forward(2.5);
  leftForward(2.5);
  delay(50);
  turnLeft(1.1);
  delay(50);
  driveForward();
  forward(2);
  delay(50);
  openClamp();
  delay(50);
  driveReverse();
  forward(2);
  rightForward(1.7);
  forward(2.5);
  rightForward(1.7);
  forward(2.5);
  
}

void cyber()//cyber mission
{
  while (digitalRead(2)==LOW)
  {
    
  }
  //int thresh=analogRead(0);
  delay(200);
  driveReverse();
  forward(1);
  while (analogRead(1)>940)
  {
    forward();
  }
  long cyberTime=millis();
  while (millis()-cyberTime<52500)
  {
    Serial.println(millis()-cyberTime);
    if (analogRead(1)>940)
    {
      rightWheel.writeMicroseconds(1420);
      leftWheel.writeMicroseconds(1520);
    }
    else
    {
      leftWheel.writeMicroseconds(1500);
      rightWheel.writeMicroseconds(1700);
    }


  }
  halt();
}
void photoTest()
{
  while (1==1)
  {
  Serial.print("left light= ");
  Serial.print(analogRead(0));
  Serial.print("right light= ");
  Serial.println(analogRead(1));
  }
}
void setup() {
  // put your setup code here, to run once:
  delay(500);
  Serial.begin(9600);
  //photoTest();
  leftWheel.attach(4);
  rightWheel.attach(3);
  spinner.attach(8);
  nano();
  chemical();
  civil();
  //bio();
  //mech();
  //electrical();
  
  cyber();
  spinner.detach();
  
  Serial.println("end of setup");
  

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("loop");
  
}
