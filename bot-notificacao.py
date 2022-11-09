import telegram_send 
import threading
import time

#etapas para instalação
#https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580

def verificarVazamentoSensor1():
    print("ENVIAR NOTIFICACAO SENSOR 1 INICIADO")
    while True:
        meuArquivo = open('dados-sensor1.csv')
        nomes = meuArquivo.readlines()
        linha = nomes[-1]

        if linha >= "0.23":
            telegram_send.send(messages=["Vazamento Sensor 1"])
            print("ENVIADO NOTIFICAÇÃO DE VAZAMENTO SENSOR 1")
        time.sleep(2)

def verificarVazamentoSensor2():
    print("ENVIAR NOTIFICACAO SENSOR 2 INICIADO")
    while True:
        meuArquivo = open('dados-sensor2.csv')
        nomes = meuArquivo.readlines()
        linha = nomes[-1]

        if linha >= "0.23":
            telegram_send.send(messages=["Vazamento Sensor 2"])
            print("ENVIADO NOTIFICAÇÃO DE VAZAMENTO SENSOR 2")
        time.sleep(2)

if __name__ == "__main__":
    x = threading.Thread(target=verificarVazamentoSensor1)
    x.start()
    y = threading.Thread(target=verificarVazamentoSensor2)
    y.start()
   


