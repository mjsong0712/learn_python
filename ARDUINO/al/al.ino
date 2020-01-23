#include <SoftwareSerial.h>
SoftwareSerial BTSerial(2, 3);
int led1 = 7;
int led2 = 4;
int boozer = 8;
int al = A0;
int value;


void setup() {  
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(boozer, OUTPUT);
}

void loop() {
 /*if (BTSerial.available()){
    char data = BTSerial.read();
    Serial.write(data);
    
    if(data == '0'){
      digitalWrite(13, HIGH);
    }else if(data == '1'){
      digitalWrite(13, LOW);
    }
  }*/
  
 value = analogRead(al);
 BTSerial.println(value);
 Serial.println(value);
 /*if (value < 85) {
  digitalWrite(boozer, HIGH);
  digitalWrite(led2, HIGH);
  digitalWrite(led1, LOW);
 }  else{
  digitalWrite(boozer, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led1, HIGH);4
   if (Serial.available()){
  BTSerial.write(Serial.read());
   }
 }*/
 delay(300);
}
