long int Time;
int emg;

void setup() {
  Serial.begin(9600);

}

void loop() {
  emg=analogRead(A0);
  Time=millis();
  Serial.print(Time);
  Serial.print(',');
  Serial.println(emg);

}
