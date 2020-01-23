#include<Servo.h>
Servo Biteservo; 
int trig = 3;
int echo = 4;
int motor = 5;
int jodo = A0;
int led = 7;
int duration;
int distance;
void setup() {
  Biteservo.attach(motor);
  pinMode(led,OUTPUT);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);  
Serial.begin(9600);
}

void loop() {
  int jodoValue = analogRead(jodo);
  Serial.println("#######");
  Serial.println(jodoValue);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  duration = pulseIn(echo, HIGH);
  distance = duration*0.034/2;
  Serial.println(distance);
  if(distance < 10){
     if (jodoValue > 220) {    
      digitalWrite(led, HIGH);
      }
      Biteservo.write(30);
      delay(2000); 
      Biteservo.write(60);
      digitalWrite(led,LOW);
  }
  delay(500);
  

  
}
