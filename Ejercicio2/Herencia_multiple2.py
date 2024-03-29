class Pared:
    def __init__(self, name, value = 0):
        self.name = name
        self.value = 0

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

class Ventana(Pared):
    def __init__(self, pared, value):
        self.pared = pared.get_name()
        pared.set_value(value)
        self.value = value

class Casa(Pared):
    def __init__(self, pared):
        self.paredes = [pared[0],pared[1],pared[2],pared[3]]
        self.sup_pared0 = pared[0].get_value()
        self.sup_pared1 = pared[1].get_value()
        self.sup_pared2 = pared[2].get_value()
        self.sup_pared3 = pared[3].get_value()



    def superficie_acristalada(self):
        superficie_total = self.sup_pared1 + self.sup_pared2 + self.sup_pared3 + self.sup_pared0
        return superficie_total


# Instanciación de las paredes
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Instanciación de las ventanas
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)


casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_acristalada())
