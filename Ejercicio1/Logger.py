class Logger:

    def __init__(self, message):
        self._message = message

    def log(self):
        return self._message

class Test(Logger):
    def llamada(self, frase):
        self.frase = frase
        if self.frase == "Primera llamada":
            self.frase = "$> cat log.txt \n--Start log-- \nPrimera llamada"
        else:
            self.frase =+ "\n" + log()
    
        return self.frase



test = Test() 
for i in range(1, 6): 
   if i == 1: 
       test.llamada("Primera llamada") 
   else: 
       test.llamada("{}ª llamada".format(string)) 