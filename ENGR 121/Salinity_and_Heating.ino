

//#9
//George Cazenavette, Ryan Vedros, James Cole Dewitt
//Dr. Swanbom
//HNRS 121 H05

#include <math.h>

#define e 2.7182818284590452353602874713527

double setpoint=.001;

double tempSetpoint = 25;

int sensor=0;

int heat = 5;

int therm = 1;

int di=9;

int salty=8;

double output[]={0,0,0,0,0};

double avgoutput=0;

int counter=0;

double OF=.8;

double mass=65.89629424;

double addedmass=0;

double topen=0;

long deadtime=9000;

long tlast=0;

double diflow=8.32;

double saltyflow=6.73;

double sigma=3.199917762;

//in C, log(x) is the natural log of x
double setvalue=141.4450*log(setpoint)+1646.0847;

double ucl=setvalue+3*sigma;

double lcl=setvalue-3*sigma;

double uclDec = pow(e, (ucl - 1646.0847) / 141.4450);

double lclDec = pow(e, (lcl - 1646.0847) / 141.4450);

double salinity=0;

double target=0;

double gain=.9;

double fixoutput=0;

int temp3Sigma = 1;

int tempUCL = int(9.03903*tempSetpoint+273.73116+temp3Sigma+.5);

int tempLCL = int(9.03903*tempSetpoint+273.73116-temp3Sigma+.5);

double tempUCLdeg = (tempUCL - 273.73116)/9.03903;

double tempLCLdeg = (tempLCL - 273.73116)/9.03903;

void setup() {
  // initializes pins and LCD
  Serial.begin(9600);
  pinMode(1,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(5, OUTPUT);
  Serial.write(12);
  Serial.write(17);
  Serial.write(132);
  Serial.print("LCL    SP   UCL");
  Serial.write(148);
  Serial.print("S:");
  Serial.write(168);
  Serial.print("T:");
  Serial.write(188);
  Serial.print("S=      T=     H=on");
  Serial.write(151);
  Serial.print(100*lclDec, 3);
  Serial.write(157);
  Serial.print(100*setpoint, 3);
  Serial.write(163);
  Serial.print(100*uclDec, 3);
  Serial.write(172);
  Serial.print(tempLCLdeg, 1);
  Serial.write(178);
  Serial.print(tempSetpoint, 1);
  Serial.write(184);
  Serial.print(tempUCLdeg, 1);
  Serial.write(22);
  //establishes an initial baseline before the system checks itself
  for (int i=0;i<5; i++)
  {
    digitalWrite(3,HIGH);
    delay(100);
    output[i]=analogRead(sensor);
    digitalWrite(3,LOW);
    delay(100);
  }
}

void loop() {
  
  digitalWrite(3,HIGH);
  delay(100);
  output[counter]=analogRead(sensor);
  digitalWrite(3,LOW);
  
  //rolling average
  avgoutput=(output[0]+output[1]+output[2]+output[3]+output[4])/5;
  salinity=pow(e,(avgoutput-1646.0847)/141.4450);
  Serial.write(190);
  Serial.print(100*salinity,3);


  //adds salt water if the salinity is below the LCL
  if (millis()-tlast>deadtime && avgoutput<lcl)
  {
    salinity=pow(e,(avgoutput-1646.0847)/141.4450);
    target=salinity+(setpoint-salinity)*gain;
    addedmass=(mass*(target-salinity))/((1-OF)*(0.01-salinity));
    topen=1000*addedmass/saltyflow;
    digitalWrite(salty,HIGH);
    delay(long(topen));
    digitalWrite(salty,LOW);
    tlast=millis();
  }
  
  //adds DI water if salinity is over the UCL
  if (millis()-tlast>deadtime && avgoutput>ucl)
  {
    salinity=pow(e,(avgoutput-1646.0847)/141.4450);
    target=salinity-(salinity-setpoint)*gain;
    addedmass=(mass*(salinity-target))/((1-OF)*(salinity));
    topen=1000*addedmass/diflow;
    digitalWrite(di,HIGH);
    delay(long(topen));
    digitalWrite(di,LOW);
    tlast=millis();
  }
  
  delay(100);
  //regulates heater
  if (analogRead(therm) > tempUCL)
  {
    digitalWrite(heat, LOW);
    Serial.write(205);
    Serial.print("off");
  }
  else if (analogRead(therm) < tempLCL)
  {
    digitalWrite(heat, HIGH);
    Serial.write(205);
    Serial.print("on ");
  }

  Serial.write(198);
  Serial.print((analogRead(therm)-273.73116)/9.03903,1);
  delay(900);
  
  //keeps a counter for the rolling average
  counter=counter+1;
  if (counter==5)
  {
    counter=0;
  }

}
