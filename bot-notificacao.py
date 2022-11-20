import telegram_send 
import threading
import time

#etapas para instalação
#https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580
fome = True
contador = 0

def mandarMsg():
    print("ENVIAR NOTIFICACAO SENSORES INICIADO")
    while True:
        global fome
        global contador
        ler1 = open('dados-sensor1.csv')
        dados = ler1.readlines()
        sensor1 = dados[-1]

        ler2 = open('dados-sensor2.csv')
        dados2 = ler2.readlines()
        sensor2 = dados2[-1]

        diferenca = float(sensor1) - float(sensor2)

        if diferenca > 0.03:
            contador +=1
            if contador == 21600:
              contador = 0
              telegram_send.send(messages=["Possível vazamento na tubulação"])
              print("ENVIADO NOTIFICAÇÃO DE VAZAMENTO SENSORES")
            if fome: 
                telegram_send.send(messages=["Possível vazamento na tubulação"])
                print("ENVIADO NOTIFICAÇÃO DE VAZAMENTO SENSORES")
                fome = False     
        elif diferenca < 0.03:
            contador = 0
            fome = True
                    
        #tempo de leitura dos arquivos
        time.sleep(2)

if __name__ == "__main__":
    #x = threading.Thread(target=verificarVazamento)
    #x.start()
    y = threading.Thread(target=mandarMsg)
    y.start()
