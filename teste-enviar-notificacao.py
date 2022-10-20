import telegram_send 

class TelegramBot:
    def __init__(self):
        self.fluxo = 20

        if self.fluxo == 20:
            telegram_send.send(messages=["Nossa, foi fácil!"])

bot = TelegramBot()


#if self.fluxo >= 100:
    #telegram_send.send(messages=["Vazamento!!!!"])

#https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580


