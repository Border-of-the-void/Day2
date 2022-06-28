import serial
ok = True
time_0=time_1=0
x=1
try:
    ser = serial.Serial ('COM6', 9600)
except Exception:
    print('Проверьте порт')
    ok = False
run = True

if ok:
    print('Успешно')
    while run:
        try:
            t, emg = ser.readline().decode('utf8').strip().split(',')
            emg=int(emg)
            t=int(t)
            if emg > 800 and t>(time_0+300):
                time_1=time_0
                time_0=t
                x=time_0-time_1
            print(60000//x)
        except:
            print('Поломка')
            run = False            
    ser.close() 
