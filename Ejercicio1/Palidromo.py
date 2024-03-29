class Palindromo():

    def __init__(self, palabra, atributo = " "):
        self.palabra = palabra
        self.atributo = atributo #No entendi exactamente lo que me pedian en el ejercicio de palindromo - metodo instancia

    def get_palabra(self):
        return self.palabra

    def esPalindromo(self):
        palabra = self.palabra.replace(' ', '').lower()
        for i in range(len(palabra)-1):
            if palabra[i] == palabra[-i-1]:
                continue
            else:
                return False
        return True

    def test(self):
        palabra_atributo = str(self.atributo).replace(' ', '').lower()
        for i in range(len(palabra_atributo)//2):
            if palabra_atributo[i] != palabra_atributo[-i-1]:
                return False
            else:
                return True
    
    def palabra_mayuscula(self):
        print(self.atributo.upper())


print(Palindromo.esPalindromo(Palindromo('radar')))
# >>> True
p = Palindromo("radar") 
print(p.test()) 
