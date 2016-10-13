#include <math.h>

#define e 2.7182818284590452353602874713527

int sensor=0;

int di=9;

int salty=8;

double output[]={0,0,0,0};

double avgoutput=0;

int counter=0;

double OF=.9;

double mass=65.89629424;

double addedmass=0;

double topen=0;

long deadtime=5000;

long tlast=0;

double diflow=8.32;

double saltyflow=6.73;

double sigma=3.199917762;

double setpoint=.001;

double setvalue=141.4450*log(setpoint)+1646.0847;

double ucl=setvalue+3*sigma;

double lcl=setvalue-3*sigma;

double salinity=0;

double target=0;

double gain=.9;

void setup() {
  // put your setup code here, to run once:
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
  Serial.print("Status=checking");
  Serial.write(22);
  for (int i=1;i<3; i++)
  {
    digitalWrite(3,HIGH);
    delay(100);
    output[i]=analogRead(sensor);
    digitalWrite(3,LOW);
    delay(100);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (counter==3)
  {
    counter=0;
  }
  digitalWrite(3,HIGH);
  delay(100);
  output[counter]=analogRead(sensor);
  digitalWrite(3,LOW);
  avgoutput=(output[0]+output[1]+output[2])/3;
  salinity=pow(e,(avgoutput-1646.0847)/141.4450);
  Serial.write(137);
  Serial.print(salinity*100,4);
  Serial.write(143);
  Serial.print("%wt");
  if (millis()-tlast>deadtime && avgoutput<lcl)
  {
    delay(3000);
    digitalWrite(3,HIGH);
    delay(100);
    salinity=analogRead(sensor);
    digitalWrite(3,LOW);
    target=salinity+(setpoint-salinity)*gain;
    addedmass=(mass*(target-salinity))/((1-OF)*(0.01-salinity));
    topen=1000*addedmass/saltyflow;
    Serial.write(180);
    Serial.print("open  ");
    Serial.write(195);
    Serial.print("adding salty");
    digitalWrite(salty,HIGH);
    delay(topen);
    digitalWrite(salty,LOW);
    Serial.write(180);
    Serial.print("closed");
    Serial.write(195);
    Serial.print("checking    ");
    tlast=millis();
  }

  if (millis()-tlast>deadtime && avgoutput>ucl)
  {
    delay(3000);
    digitalWrite(3,HIGH);
    delay(100);
    salinity=analogRead(sensor);
    digitalWrite(3,LOW);
    target=salinity-(setpoint-salinity)*gain;
    addedmass=(mass*(target-salinity))/((1-OF)*(salinity));
    topen=1000*addedmass/diflow;
    Serial.write(160);
    Serial.print("open  ");
    Serial.write(195);
    Serial.print("adding DI");
    digitalWrite(di,HIGH);
    delay(topen);
    digitalWrite(di,LOW);
    Serial.write(160);
    Serial.print("closed");
    Serial.write(195);
    Serial.print("checking    ");
    tlast=millis();
  }
  delay(100);

}
