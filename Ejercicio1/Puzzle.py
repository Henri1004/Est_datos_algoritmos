"""""
Enunciado: adivina qué mensajes se muestran mediante el siguiente código voluntariamente poco comprensible:
"""""

class A:
    def z(self):
        return self

    def y(self, t):
        return len(t)

a = A # asigna una clase "A" a "a"
y = a.z #la variable y, es igual al metodo z de la clase A
print(y(a)) # Imprime y(a), es decir el self >>> <class  main>
aa = a()
print(aa is a())# imprime False, la verdad es que yo habria dicho que da True
z = aa.y # realiza el metodo, que es la longitud de la lista
print(z(())) # z es igual a aa, y aa es igual que a, la variable a no tiene datos, con lo cual, devolvera 0
print(a().y((a,))) # el metodo y contiene una tupla (a,), luego en vez de devolver 0, devolvera 1
print(A.y(aa, (a,z))) # aqui tenemos una tupla y la instancia aa, luego devolvera 2
print(aa.y((z,1,'z'))) # En la ultima hay tres datos, luego devolvera 3

# este codigo imprime lo siguiente:
    #<class main>
    #False(pero no se porque)
    #0
    #1
    #2
    #3