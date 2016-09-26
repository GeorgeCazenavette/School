int val = 0;
int heat = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(5,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(1);
  Serial.println(val);
  if (val < 513)
  {
    digitalWrite(5, HIGH);
  }
  else
  {
    digitalWrite(5, LOW);
  }

}
