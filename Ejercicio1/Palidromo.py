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
    

print(Palindromo.esPalindromo(Palindromo('radar')))
# >>> True
