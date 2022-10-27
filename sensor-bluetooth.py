from dataclasses import dataclass
import bluetooth
import pandas as pd

#Depois de instalar as dependencias pra biblioteca pybluez, instalar a biblioteca manualmente na pasta dela.
#comando: python setup.py install

bd_addr = "00:19:07:00:39:ab"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('DISPOSITIVO BLUETOOTH CONECTADO')

arquivo = "dados.csv"
#amostra = 10
#linha = 0

dados = []
dados2 = []

while True:
    data = str(sock.recv(409600000).decode('utf-8'))
    
    print(data)

    file = open(arquivo, "a")
    file.write(data)
    #linha = linha+1

#print("TERMINOU DE LER")
#file.close()
#threading.Thread(target=teste).start()







