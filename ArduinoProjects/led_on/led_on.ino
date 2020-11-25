const int buzzer = 8;
int value = 0;
void setup(){
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}
void loop(){
  value = analogRead(A5);
  Serial.println(value*6.8);
  noTone(buzzer);

}
