import sys
import subprocess

from requests import delete

arquivos = ['receber-bluetooth.py', 'receber-sensores.py', 'bot.py', 'bot-notificacao.py']
processos = []

for arquivo in arquivos:
    processo = subprocess.Popen([sys.executable, arquivo])
    processos.append(processo)

# neste ponto todos os scripts estão rodando em background ao mesmo tempo. 
# Vamos esperar todos eles terminarem:

for processo in processos:
    processo.wait()