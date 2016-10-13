void setup() {
   Serial.begin(9600);                   // use a baud rate of 9600 bps 
   pinMode(1,OUTPUT);                    // set pin1 as an output (pin1=TX)
   Serial.write(12);                     // clear screen & move to top left position
   Serial.write(129);                    // move cursor to row 0, position 1
   Serial.write("Temperature Sensor");   // print a text string starting at (0,1)
   Serial.write(152);                    // move cursor to row 1, position 4
   Serial.write("Calibration");          // print a text string starting at (1,4)
   Serial.write(189);                    // move cursor to row 3, position 1
   Serial.write("analog input=");        // print  text string at (3,1)   
   Serial.write(22);                     // turn cursor off to keep screen clean   
}

void loop() {

   int analogT;       // declare analogT as an integer
   analogT=analogRead(1);    // read the voltage at analog pin 4

   Serial.write(202);                    // move cursor to row 3, position 14
   Serial.print(analogT);                // print the analog input reading (0 to 1023) 
   delay(2500);
   Serial.write(202);                   // overwrite previously printed numbers
   Serial.write("   ");
   delay(500);
}

