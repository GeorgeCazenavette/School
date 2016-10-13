
//AutoBox Arduino Code

void setup() {
  // sets states of digital pins
  pinMode(5, INPUT);
  pinMode(4, OUTPUT);
  pinMode(6, INPUT);
}

void loop() {
// activates the relay if the safety pin is LOW and the control pin is HIGH
if (digitalRead(6) && !digitalRead(5))
{
  digitalWrite(4, HIGH);
}
 else
 {
  digitalWrite(4, LOW);
 }
}
