int val=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(11,OUTPUT);
  val=analogRead(3);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(val);
  if (val<600)
  {
    digitalWrite(11,HIGH);
    delay(100);
    digitalWrite(11,LOW);
    delay(100);
  }
  
  if (analogRead(3)<val-2)
  {
    digitalWrite(13,HIGH);
    delay(300);
    digitalWrite(13,LOW);
    delay(300);
  }
  val=analogRead(3);
   
}
