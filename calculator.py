# Calculadora (main)
import complexconv
import complexinput #cli
import complexoperations

# Ejemplos válidos
#3+2i
#3cis(120°)
#3e^i3/2pi
def detectar(z,n):
    print("z" + str(n) + " es ", end="")
    match complexinput.tipo(z):
        case 1:
            print("BINÓMICA")
        case 2:
            print("POLAR")
        case 3:
            print("EXPONENCIAL")

z1 = input("Ingresa el 1er número complejo:\n")
detectar(z1,1)
z2 = input("Ingresa el 2do número complejo:\n")
detectar(z2,2)

# === Tests ===
print("suma (+)::   ", end="")
print(complexoperations.adicion(z1,z2,0))
print("resta (-)::   ", end="")
print(complexoperations.adicion(z1,z2,1))
print("multiplicación (*)::   ", end="")
print(complexoperations.factor(z1,z2,0))
print("división (/)::   ", end="")
print(complexoperations.factor(z1,z2,1))
print("potencia (**)::   ", end="")
print(complexoperations.potencia(z1,2,0))
print("raiz (**1/n)::   ", end="")
print(complexoperations.potencia(z1,2,1))




'''
======== PARTE DEL MENÚ ARCHIVADA POR ENFOQUE AL DISEÑO GUI ========


print("====================================")
print("     OPERACIÓN A REALIZAR")
print("====================================")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Potencia  n-ésima")
print("6. Raíz      n-ésima")
print("====================================")
'''
#op = input()
#while op.isdigit() == False and int(op) < i and int(op) > 6:
 #   print("Opción inválida, ingrese una opción [1-6]")
  #  op = input()
#op = int(op)
op = 90

match op:
    case 1:
        print(complexoperations.adicion(z1,z2,0))
    case 2:
        print(complexoperations.adicion(z1,z2,1))
    case 3:
        print(complexoperations.factor(z1,z2,0))
    case 4:
        print(complexoperations.factor(z1,z2,1))
    case 5:
        print(complexoperations.potencia(z1,2,0))
    case 6:
        print(complexoperations.potencia(z1,2,1))
'''