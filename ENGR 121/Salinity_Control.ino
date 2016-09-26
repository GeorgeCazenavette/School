//#7
//George Cazenavette, Ryan Vedros, James Cole Dewitt
//Dr. Swanbom
//HNRS 121 H05

#include <math.h>

#define e 2.7182818284590452353602874713527

int sensor=0;

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

double setpoint=.001;

//in C, log(x) is the natural log of x
double setvalue=141.4450*log(setpoint)+1646.0847;

double ucl=setvalue+3*sigma;

double lcl=setvalue-3*sigma;

double salinity=0;

double target=0;

double gain=.9;

double fixoutput=0;

void setup() {
  // initializes pins and LCD
  Serial.begin(9600);
  pinMode(1,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  Serial.write(12);
  Serial.write(128);
  Serial.print("Salinity=");
  Serial.write(151);
  Serial.print("DI valve=closed");
  Serial.write(168);
  Serial.print("Salty valve=closed");
  Serial.write(188);
  Serial.print("Status:output=     ");
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
  Serial.write(137);
  Serial.print(salinity*100,4);
  Serial.write(143);
  Serial.print("%wt");
  Serial.write(201);
  Serial.print(avgoutput,0);

  //adds salt water if the salinity is below the LCL
  if (millis()-tlast>deadtime && avgoutput<lcl)
  {
    digitalWrite(3,HIGH);
    delay(100);
    fixoutput=avgoutput;
    salinity=pow(e,(fixoutput-1646.0847)/141.4450);
    digitalWrite(3,LOW);
    target=salinity+(setpoint-salinity)*gain;
    addedmass=(mass*(target-salinity))/((1-OF)*(0.01-salinity));
    topen=1000*addedmass/saltyflow;
    Serial.write(180);
    Serial.print("open  ");
    Serial.write(195);
    Serial.print("adding salty");
    Serial.write(137);
    Serial.print("mixing");
    digitalWrite(salty,HIGH);
    delay(long(topen));
    digitalWrite(salty,LOW);
    Serial.write(180);
    Serial.print("closed");
    Serial.write(195);
    Serial.print("output=     ");
    tlast=millis();
  }

  //adds DI water if salinity is over the UCL
  if (millis()-tlast>deadtime && avgoutput>ucl)
  {
    digitalWrite(3,HIGH);
    delay(100);
    fixoutput=avgoutput;
    salinity=pow(e,(fixoutput-1646.0847)/141.4450);
    digitalWrite(3,LOW);
    target=salinity-(salinity-setpoint)*gain;
    addedmass=(mass*(salinity-target))/((1-OF)*(salinity));
    topen=1000*addedmass/diflow;
    Serial.write(160);
    Serial.print("open  ");
    Serial.write(195);
    Serial.print("adding DI");
    Serial.write(137);
    Serial.print("mixing");
    digitalWrite(di,HIGH);
    delay(long(topen));
    digitalWrite(di,LOW);
    Serial.write(160);
    Serial.print("closed");
    Serial.write(195);
    Serial.print("output=     ");
    tlast=millis();
  }
  delay(100);
  
  //keeps a counter for the rolling average
  counter=counter+1;
  if (counter==5)
  {
    counter=0;
  }

}
