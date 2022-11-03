import threading
import time

def lersensor1():
    while True:
        with open('dados-2sensores.csv') as f:
            sensor = str(f.readlines())
            splitSen = sensor.split(';') 

        sensorA = []
        sensorB = []

        for i in range(len(splitSen)):
            #print(splitSen[i])
            split = splitSen[i].split(',')
            if len(split) != 1:
                sensorA.append(split[0])
                sensorB.append(split[1])

        arquivo = "dados-sensor1.csv"
        file = open(arquivo, "a")
        file.write(sensorA[-1] + "\n")
        time.sleep(0.8)

def lersensor2(): 
    while True:
        with open('dados-2sensores.csv') as f:
            sensor = str(f.readlines())
            splitSen = sensor.split(';') 

        sensorA = []
        sensorB = []

        for i in range(len(splitSen)):
            #print(splitSen[i])
            split = splitSen[i].split(',')
            if len(split) != 1:
                sensorA.append(split[0])
                sensorB.append(split[1])

        arquivo = "dados-sensor2.csv"
        file = open(arquivo, "a")
        file.write(sensorB[-1] + "\n")
        time.sleep(0.8)

if __name__ == "__main__":
    x = threading.Thread(target=lersensor1)
    x.start()
    y = threading.Thread(target=lersensor2)
    y.start()



