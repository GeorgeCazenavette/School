int deviationTest=0;


void setup() {
   Serial.begin(9600);                     // use a baud rate of 9600 bps 
   pinMode(1,OUTPUT);                     // set pin1 as an output (pin1=TX)
   Serial. write(12);                 // clear screen & move to top left position
   Serial. write(128);                // move cursor to row 0, position 1
   Serial. write("Conductivity Sensor");  // print a text string starting at (0,1)
   Serial. write(152);                // move cursor to row 1, position 4
   Serial. write("Calibration");            // print a text string starting at (1,4)
   Serial. write(189);                // move cursor to row 3, position 1
   Serial. write("analog input=");        // print  text string at (3,1)   
   Serial. write(22);                 // turn cursor off to keep screen clean   
   pinMode(3, OUTPUT);   
   if (deviationTest==1)
   {
    double total=0;
    double readings[]={};
    for (int i=0; i<10;i++)
    {
    delay (100);
    digitalWrite(3,HIGH);                  // apply 5V to the conductivity sensor
    delay(100);                            // hold the voltage at pin 3 for 0.1s
    double analogS=double(analogRead(0));             // read voltage on + side of 10kohm resistor
    digitalWrite(3,LOW);                   // turn off power to the conductivity sensor
    Serial.write(202);                 // move cursor to row 3, position 14
    Serial.print(analogS);                 // print the analog input reading (0 to 1023) 
    Serial.write("  ");                    // overwrite previously printed numbers
    delay(1000);                           // delay 1 second between measurements
    readings[i]=analogS;   
    total=total+analogS;
    }
    double average=total/10.0;
    double std=0;
    for (int i=0;i=10;i++)
    {
      std=std+sq(readings[i]-average);
    }
    std=sqrt(std/9);
    Serial.write(168);
    Serial.print(8008,2);
   }
   //Serial.print(average)
}

void loop() {
   if (deviationTest==0)
   {
   digitalWrite(3,HIGH);                  // apply 5V to the conductivity sensor
   delay(100);                            // hold the voltage at pin 3 for 0.1s
   int analogS=analogRead(0);             // read voltage on + side of 10kohm resistor
   digitalWrite(3,LOW);                   // turn off power to the conductivity sensor
   Serial.write(202);                 // move cursor to row 3, position 14
   Serial.println(analogS);                 // print the analog input reading (0 to 1023) 
   Serial.write("  ");                    // overwrite previously printed numbers
   delay(900);                           // delay 1 second between measurements
   }
}

