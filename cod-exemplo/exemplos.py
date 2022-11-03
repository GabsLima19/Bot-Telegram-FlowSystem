import time

class dados:
  def __init__(self, a):
    self.a = a
    
  def sum(self):
    while True:
      self.a = self.a + 1
      time.sleep(0.2)
      print (self.a)

if __name__ == "__main__":
    obj = dados(0)
    obj.sum()



#meuArquivo = open('dados-sensor1.csv')
#nomes = meuArquivo.readlines()
#print(nomes[-1])