class Base: 
 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 
 
class Derivada(Base): 
 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
 
base = Base() #asigna una clase Base a base
derivada = Derivada() #asigna una clase Derivada a derivada
 
base.A() # estas utilizando el metodo A, es decir imprimes self.a = a
derivada.A() # hace lo mismo que el anterior
print() # imprime un espacio
base.B() # estas utilizando el metodo B de la clase Base, es decir imprimes b
derivada.B() # estas utilizando el metodo B de la clase Derivada, es decir imprimes bb
base.C() # imprime c
derivada.C() #imprime cc
derivada = base 
derivada.C()#imprime c

#Este codigo imprime lo siguiente:
    #a
    #a
    #
    #b
    #bb
    #c
    #cc
    #c
    