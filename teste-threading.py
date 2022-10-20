from pprint import pprint
import threading
import time

def teste():
    for i in range(100):
        print(i, "teste")
        time.sleep(1)


threading.Thread(target=teste).start()

def teste30():
    for i in range(100):
        print(i, "teste")
        time.sleep(1)

threading.Thread(target=teste30).start()
