# Calculadora (main)
#import complexconv
#import complexinput
#import complexoperations

# NUEVOS NOMBRES
import conv
import cli
import operations

# Pedir números complejos e imprimir el tipo detectado
cli.cl('g')
z1 = input("Ingresa el 1er número complejo:\n")
cli.cl('y')
cli.imprimir_tipo(z1,1)

cli.cl('g')
z2 = input("Ingresa el 2do número complejo:\n")
cli.cl('y')
cli.imprimir_tipo(z2,2)



# === Tests ===
# Imprimir los resultados para todas las operaciones
cli.cl('r')
print("::suma (+)::")
cli.cl()
print(operations.adicion(z1,z2,0))

cli.cl('b')
print("::resta (-)::")
cli.cl()
print(operations.adicion(z1,z2,1))

cli.cl('g')
print("::multiplicación (*)::")
cli.cl()
print(operations.factor(z1,z2,0))

cli.cl('y')
print("::división (/)::")
cli.cl()
print(operations.factor(z1,z2,1))

cli.cl('r')
print("::potencia (**)::")
cli.cl()
print(operations.potencia(z1,2,0))

cli.cl('b')
print("::raiz (**1/n)::")
cli.cl()
print(operations.potencia(z1,2,1))