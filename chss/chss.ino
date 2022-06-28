long int Time; // переменная для хранения времени
int emg;  // переменная для хранения электромиаграммы

void setup() {
  Serial.begin(9600); // скорость отправки данных в Python 

}

void loop() {
  emg=analogRead(A0); // запись электромиаграммы 
  Time=millis(); // запись времени прошедшего с начала запуска программы
  Serial.print(Time); // отправка времени прошедшего с начала запуска программы в Python
  Serial.print(',');
  Serial.println(emg); // отправка электромиаграммы в Python 

}
