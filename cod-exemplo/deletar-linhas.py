import time
import threading

def apagarGeral():
    while True:
        with open("dados.csv", 'r+') as f:
            time.sleep(60)
            f.truncate(0)
            print("Dados total APAGADO")

def apagarDados1():
    print("APAGAR LINHAS INICIADO")
    while True:
        with open("dados-sensor1.csv", 'r+') as f:
            time.sleep(60)
            f.truncate(0)
            time.sleep(60)
            print("Dados sensor 1 APAGADO")

def apagarDados2():
    while True:
        with open("dados-sensor2.csv", 'r+') as f:
            time.sleep(60)
            f.truncate(0)
            time.sleep(60)
            print("Dados sensor 2 APAGADO")

if __name__ == "__main__":
    x = threading.Thread(target=apagarDados1)
    x.start()
    y = threading.Thread(target=apagarDados2)
    y.start()
    #z = threading.Thread(target=apagarGeral)
    #z.start()

