void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(300);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(300);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(300);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(300);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(300);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(13, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(12, HIGH);
  digitalWrite(13, LOW);
  delay(50);
  digitalWrite(12, LOW);
  digitalWrite(13, HIGH);
  delay(50);
}
