void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.write(128);
  Serial.write("CONDUCTIVITY SENSOR");
  Serial.write(152);
  Serial.write("CALIBRATION");
  Serial.write(189);
  Serial.write("analog input=");
  
}
void loop() {
  // put your main code here, to run repeatedly:
  for (int i=1;i<=15;i++)
  {
    Serial.write("  ");
    Serial.write(202);
    Serial.print(i);
    delay(1000);
  }
}
