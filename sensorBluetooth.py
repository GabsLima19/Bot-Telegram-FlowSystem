from dataclasses import dataclass
import bluetooth
import threading

bd_addr = "00:19:07:00:39:ab"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('DISPOSITIVO BLUETOOTH CONECTADO')

print("inicio")

def teste():
    while True:
        data = sock.recv(409600000)
        print(str(data.decode('utf-8')))

threading.Thread(target=teste).start()

print("fim")






