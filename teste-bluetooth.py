from dataclasses import dataclass
import bluetooth
import struct

bd_addr = "00:19:07:00:39:ab"
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('Conectado')

while True:
    data = sock.recv(409600000)
    print(data.decode('utf-8'))
