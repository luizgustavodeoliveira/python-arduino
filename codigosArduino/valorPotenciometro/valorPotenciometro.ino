#define ponteiroPot A0

const int delayTime = 500;

void setup() {
  pinMode(ponteiroPot, INPUT);
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(ponteiroPot));
  delay(delayTime);
}
