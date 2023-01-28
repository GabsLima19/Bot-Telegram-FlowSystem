#imports bot
import requests
import time
import json
import os
#import telegram_send
#from recebersensores import lersensor1
import threading
   
#COMEÇOBOT
class TelegramBot:
    def __init__(self):
        iTOKEN  = '5529270761:AAHeMjcqw_MIrvymA8LkIdlF7E4st5L0jq0'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'
        #self.sensor1 = lersensor1()
        #self.sensor2 = 100
  
    #funções bot             
    def Iniciar(self):
        print('BOT INICIADO COM SUCESSO')
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    #threading.Thread(target=Iniciar).start()

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))

        if primeira_mensagem == True or mensagem.lower() in (''):
            return f'''O que deseja saber?{os.linesep}1- Fluxo de água atual{os.linesep}2- Fluxo total{os.linesep}'''

        if mensagem == '1':
            meuArquivo = open('dados-sensor1.csv')
            nomes = meuArquivo.readlines()
            return nomes[-1]

        if mensagem == '2':
            meuArquivo = open('dados-sensor2.csv')
            nomes = meuArquivo.readlines()
            return nomes[-1]
            
        elif mensagem == '3':
            arquivo1 = open('dados-sensor1.csv')
            arquivo2 = open('dados-sensor2.csv')
            valor1 = arquivo1.readlines()
            valor2 = arquivo2.readlines()
            x = float(valor1[-1])
            y = float(valor2[-1])
            return x + y

        #elif mensagem.lower() in ('s', 'sim'):
            #return ''' Pedido Confirmado! '''
        #elif mensagem.lower() in ('n', 'não'):
            #return ''' Item não incluso! Informe o codigo do item: '''
        else:
            return f'''Olá! Meu nome é AquaFluxBot. Sou seu assistente da Flow System. O que deseja saber?{os.linesep}{os.linesep}1- Dados do Sensor 1{os.linesep}2- Dados do Sensor 2{os.linesep}3- Dados Total{os.linesep}'''


    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))


bot = TelegramBot()
bot.Iniciar() 
