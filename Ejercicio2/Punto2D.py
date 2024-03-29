class Punto2D:

    def __init__(self, X1, Y1):
        self.X = X1
        self.Y = Y1

    def traslacion(self, X2, Y2):
        self.X = self.X + X2
        self.Y = self.Y + Y2

    def __str__(self):
        return 'X: {}; Y: {}'.format(self.X, self.Y)


a = Punto2D(1, 2)
print("A = {}".format(a))

a.traslacion(-1, -2)
print("A = {}".format(a))

b = Punto2D(-3, 0)
b.traslacion(5, -1)
print("B = {}".format(b))



class Punto3D:

    def __init__(self, X1, Y1, Z1):
        self.X = X1
        self.Y = Y1
        self.Z = Z1

    def traslacion(self, X2, Y2, Z1):
        self.X = self.X + X2
        self.Y = self.Y + Y2
        self.Z = self.Z + Z1

    def __str__(self):
        return 'X: {}; Y: {}; Z: {}'.format(self.X, self.Y, self.Z)
    
c = Punto3D(1,5,-3) 
c.traslacion(0, -2, 1) 
print("C = {}".format(c))