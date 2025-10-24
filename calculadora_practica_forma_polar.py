#practica calculadora de complejo en forma polar
import math as mat
print("\n----Usted ha elegido la operar con la forma polar rcis0°-----") #introduccion al programa
print("----La calculadora solo permite numero decimales o enteros---")

#Definimos la funcion para mandarlo a llamar cada vez que lo necesitemos
def menu():
    print("\n----¿Que operacion desea hacer?------------------------------")
    print("----MULTIPLICACION(1)----------------------------------------")
    print("----DIVISION(2)----------------------------------------------")
    print("----POTENCIA(3)----------------------------------------------")
    print("----RAIZ ENESIMA(4)------------------------------------------")
    print("----SALIR(5)-------------------------------------------------")
   

menu()
orden=int(input())

#Definimos funciones para las operaciones
def multicis():
    r1=float(input("\n: Ingrese r: "))
    angulo1=int(input("1: Ingrese el angulo de la expresion: "))
    r2=float(input("2: Ingrese r de la segunda expresion: "))
    angulo2=int(input("2: Ingrese el angulo de la segunda expresion: "))

    rmulti=r1*r2
    angulosum=angulo1+angulo2
    while angulosum>360:
        angulosum=angulosum-360
    while angulosum<0:
        angulosum=angulosum+360
    print( "\nX=",rmulti,"cis",angulosum)

def division():
    r1=float(input("\n: Ingrese r: "))
    angulo1=int(input("1: Ingrese el angulo de la expresion: "))
    r2=float(input("2: Ingrese r de la segunda expresion: "))
    angulo2=int(input("2: Ingrese el angulo de la segunda expresion: "))

    rdivision=r1/r2
    angulodiv=angulo1-angulo2
    while angulodiv>360:
        angulodiv=angulodiv-360
    while angulodiv<0:
        angulodiv=angulodiv+360
    print("\nX=",rdivision,"cis",angulodiv)

def potencia():
    r1=float(input("\n: Ingrese r: "))
    angulo1=int(input("1: Ingrese el angulo de la expresion: "))
    numpotencia=float(input("ingrese el valor de la POTENCIA de su numero"))
    rpotencia=r1**numpotencia
    angulopotencia=angulo1*numpotencia
    while angulopotencia>360:
        angulopotencia=angulopotencia-360
    while angulopotencia<0:
        angulopotencia=angulopotencia+360
    print("\nX=",rpotencia,"cis",angulopotencia)

def raiz_enesima():
    r1=float(input("\n: Ingrese r: "))
    angulo1=int(input("1: Ingrese el angulo de la expresion: "))
    numraiz=int(input("Ingrese el valor de la RAIZ de su numero: "))
    r_raiz=r1**(1/numraiz)

    #gracias a este ciclo podemos obtener todos los resultados que pueden corresponder a la raiz
    i=1
    for i in range(numraiz):
        anguloraiz=(angulo1+(i*360))/numraiz
        print("\nX",(i+1),"=",r_raiz,"cis",anguloraiz)

#Este ciclo permite mantener al ususario en el menu hasta que el lo deseé
while orden!=5:
    if orden==1:
        multicis()

    elif orden==2:
        division()

    elif orden==3:
        potencia()

    elif orden==4:
        raiz_enesima()
    else: print("Valor no valido")

    menu()
    orden=int(input())





