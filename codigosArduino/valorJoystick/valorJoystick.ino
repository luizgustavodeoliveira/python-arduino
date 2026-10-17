#define valX A0
#define valY A1
#define valS 2

const int delayTime = 200;

void setup() {
  pinMode(valX, INPUT);
  pinMode(valY, INPUT);
  pinMode(valS, INPUT);
  
  Serial.begin(9600);
}

void loop() {
  Serial.print(analogRead(valX));
  Serial.print(",");
  Serial.print(analogRead(valY));
  Serial.print(",");
  Serial.println(digitalRead(valS));
  delay(delayTime);
}
