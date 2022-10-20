# função bluetooth conexão
def dadosbluetooth():
    bd_addr = "00:19:07:00:39:ab"
    port = 1

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    print('DISPOSITIVO BLUETOOTH CONECTADO')

    while True:
        data = sock.recv(409600000)
        print(data.decode('utf-8'))
        
threading.Thread(target=dadosbluetooth).start()


#imports bluetooth
from dataclasses import dataclass
import bluetooth

#import threads
import threading