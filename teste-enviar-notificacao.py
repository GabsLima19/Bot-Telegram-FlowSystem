import telegram_send 

class TelegramBot:
    def __init__(self):
        self.fluxo = 20

        if self.fluxo == 20:
            telegram_send.send(messages=["Nossa, foi fácil!"])

bot = TelegramBot()

