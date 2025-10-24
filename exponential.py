import matplotlib.pyplot as plt
import numpy as np

#Crea la proyección polar
def graficar(grados,r):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot([0, grados], [0, r], color='red', linestyle='-', label='Número Complejo', marker=('*'))
    texto_coordenadas = f'({r:.1f}, {np.degrees(grados):.0f}°)'
    ax.annotate(texto_coordenadas, 
                xy=(grados, r), 
                xytext=(grados, r + 1), # Offset text slightly above the point
                arrowprops=dict(facecolor='black', shrink=0.03, width=0.4),
                ha='center', va='bottom')
    ax.set_title("Resulado: Número Complejo", va='bottom')
    ax.set_xlabel("Parte Real")
    ax.set_ylabel("Parte Imaginaria")
    ax.yaxis.set_label_coords(-0.1, 0.5)
    ax.legend()
    plt.grid(True)
    plt.show()


print("INTRODUCIR SOLO VALORES DECIMALES")
print("NUMERO COMPLEJO 1")
pedir = input("Introduce el valor de r a operar => ")
r1 = float(pedir)
pedir = input("Introduce el valor en radianes a operar => ")
beta1 = float(pedir)
print("NUMERO COMPLEJO 2")
pedir = input("Introduce el valor de r a operar => ")
r2 = float(pedir)
pedir = input("Introduce el valor en radianes a operar => ")
beta2 = float(pedir)
print("OPERACION A REALIZAR")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Raíz n-ésima")
pedir = input("")
opc = int(pedir)
match opc:
    case 1:
        #convertir radianes a grados
        grados1 = beta1*180
        while(grados1>360):
            grados1 = grados1 - 360
        grados2 = beta2*180
        while(grados2>360):
            grados2 = grados2 - 360
        #calcular parte real e imaginaria
        a1 = r1*np.cos(beta1)
        a2 = r2*np.cos(beta2)
        b1 = r1*np.sin(beta1)
        b2 = r2*np.sin(beta2)
        #calcular las componentes del resultado
        a = a1 + a2
        b = b1 + b2
        #regresar el numero a forma polar para graficar
        r = np.sqrt(a**2+b**2)
        grados = np.arctan(b/a)
        print(grados)
        graficar(grados,r)
    case _:
        print("Opcion inválida.")
print("Vuelva pronto!")

'''
colors=grados
        fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
        sc=ax.scatter(grados, r, s=20, c=colors, cmap='hsv')
        plt.show()
        plt.show()

'''