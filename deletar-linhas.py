import time

while True:
    with open("dados.csv", 'r+') as f:
        f.truncate(0)
        time.sleep(5)
        print("dados.csv = LINHAS APAGADAS")


