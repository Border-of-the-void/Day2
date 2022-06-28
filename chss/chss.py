import serial # Импортирование библиотеки для работы с сериал портом
ok = True # отладочная переменная
time_0=time_1=0 # переменные для хранения времени
x=1 
try:
    ser = serial.Serial ('COM6', 9600) # Открытие сериал порта
except Exception:
    print('Проверьте порт') # Проверка подключения проводов и ардуино
    ok = False 
run = True # Переменная для запуска основного цикла выполнения программы 

if ok:
    print('Успешно') # Отладка если все прошло успешно 
    while run: # 
        try:
            t, emg = ser.readline().decode('utf8').strip().split(',') # запись времени и электромиограммы
            emg=int(emg) # 
            t=int(t) # 
            if emg > 800 and t>(time_0+300): # счет чсс
                time_1=time_0
                time_0=t
                x=time_0-time_1
            print(60000//x) #вывод чсс
        except:
            print('Поломка') # 
            run = False            
    ser.close() # закрытие сериал порта
