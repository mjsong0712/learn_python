int ledR = 5;
int ledG = 6;
int ledB = 9;
int ledtest = 7;
int button = 12;
int sta = 0;
void setup() {
  pinMode(ledR,OUTPUT);
  pinMode(ledG,OUTPUT);
  pinMode(ledB,OUTPUT);
  pinMode(ledtest,OUTPUT);
  pinMode(button,INPUT_PULLUP);
}

void loop() {
  if (digitalRead(button) == LOW) {
    //analogWrite(ledR,255);
    //analogWrite(ledG,255);
    //analogWrite(ledB,255);
    //digitalWrite(ledtest,HIGH);
    if (sta == 1) {
      digitalWrite(ledtest,LOW);
      sta = 0;
    } else {
      digitalWrite(ledtest,HIGH);
      sta = 1;
    }
  delay(3
  00);
  }
} 
