#include<Servo.h>
Servo Biteservo; 
int pos = 0;
int trigPin = 9;
int echoPin = 8;
int boozer = 4;
int moter = 2;
int duration;
int distance;
void setup() {
  Biteservo.attach(moter);
  pinMode(boozer, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
Serial.begin(9600);
}

void loop() {
  for(pos = 10; pos < 350; pos+=1) 
  {
    Biteservo.write(abs(pos-180));             
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    distance = duration*0.034/2;
       delay(50);
    if (distance < 20) {
      digitalWrite(boozer, HIGH);
    } else {
      digitalWrite(boozer, LOW);
    }
  }
}
  
