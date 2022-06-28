
void setup() {
  Serial.begin(115200); // скорость передачи данных в специальное ПО
}

void loop() {
  Serial.write("A0");
  Serial.write(map(analogRead(A0),0,1023,0,255)); // Отправка и маштабирование  сигнала электроэнецефалограммы
} 
