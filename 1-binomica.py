from conversor import bin_pol 
a1 = input("Ingresa el 1er coeficiente real:")
b1 = input("Ingresa el 1er coeficiente imaginario:")

a2 = input("Ingresa el 2do coeficiente real:")
b2 = input("Ingresa el 2do coeficiente imaginario:")


a1 = int(a1)
b1 = int(b1)
a2 = int(a2)
b2 = int(b2)
def suma():
    return a1+a2, b1+b2

def resta():
    return a1-a2, b1-b2

def mult():
    r1,g1 = bin_pol(a1,b1)
    r2,g2 = bin_pol(a2,b2)
    return r1*r2,g1+g2

def div():
    r1,g1 = bin_pol(a1,b1)
    r2,g2 = bin_pol(a2,b2)
    return r1/r2,g1-g2

def potencia(n):
    r,g = bin_pol(a1,b1)
    return r**n,g*n

def raiz(n):
    r,g = bin_pol(a1,b1)

    soluciones = [] # se guardan las varias soluciones en una lista
    k = 0
    while(k < n):
        p1 = r**(1/n)
        p2 = (g+360*k)/n
        soluciones.append((p1,p2))
        k+=1
    return soluciones

# pruebas
print(suma())
print(resta())

# pruebas en polar
print(mult())
print(div())
print(potencia(2))
print(raiz(3))

# LEER README.MD
#o|b|p|e
#+| |b|b
#-| |b|b
#*|p| |p
#/|p| |p
#^|p| |p
#s|p| |p
