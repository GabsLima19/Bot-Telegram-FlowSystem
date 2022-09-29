import serial, time

ard = serial.Serial('COM3', 9600)

dados = ard.readline()

while 1:
    print (dados)
    time.sleep(3)


