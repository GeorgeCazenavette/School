void setup() {
  // put your setup code here, to run once:
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=0; i<10; i++){
    digitalWrite(11, HIGH);
    digitalWrite(12, LOW);
    delay(100);
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);
    delay(100);
  }
  digitalWrite(11, LOW);
  digitalWrite(12,LOW);
  delay(1000);
  for (int i=0;i<4;i++){
    digitalWrite(11,HIGH);
    digitalWrite(12,HIGH);
    delay(300);
    digitalWrite(11,LOW);
    digitalWrite(12,LOW);
    delay(300);
  }
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  delay(500);  
}
