import requests
import time
import json
import os
import telegram_send

class TelegramBot:
    def __init__(self):
        iTOKEN  = '5498278811:AAEHRxD7ZxXKmDIxFgB2U3PTTgBTGaWDSqE'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'
        self.fluxo = 90
        self.fluxo2 = 2000

        if self.fluxo >= 100:
            telegram_send.send(messages=["Vazamento!!!!"])

    def Iniciar(self):
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

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))

        #if self.fluxo == 100:  #primeira_mensagem == True or mensagem.lower() in (''):
            #return f'''O que deseja saber?{os.linesep}1- Fluxo de água atual{os.linesep}2- Fluxo total{os.linesep}'''

        if mensagem == '1':
            return self.fluxo

        elif mensagem == '2':
            return self.fluxo2

        #elif mensagem.lower() in ('s', 'sim'):
            #return ''' Pedido Confirmado! '''
        #elif mensagem.lower() in ('n', 'não'):
            #return ''' Item não incluso! Informe o codigo do item: '''
        else:
            return f'''Olá! Meu nome é AquaFluxBot. Sou seu assistente da Flow System. O que deseja saber?{os.linesep}{os.linesep}1- Fluxo de água atual{os.linesep}2- Fluxo total{os.linesep}'''


    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))


bot = TelegramBot()
bot.Iniciar() 
