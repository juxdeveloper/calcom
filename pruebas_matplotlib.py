#en arch sudo pacman -Syu python_matplotlib (o algo asi)
#en windows se instala con pip

import matplotlib.pyplot as exp #exp es el "canvas"
import numpy as np #numpy para hacer un array con un conjunto de valores a graficar

x=np.linspace(0,2,100) #desde dónde, hasta donde, cuántos valores entre el rango

#POO
fig, ax = exp.subplots(figsize=(10,6),layout='constrained')

ax.plot(x,x, label='lineal')
ax.plot(x,x**2, label='cuadrática')
ax.plot(x,x**3, label='cúbica')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.set_title('Plot Simple')
ax.legend()

exp.show()


'''
pyplot
exp.figure(figsize=(15,7), layout='constrained')
exp.plot(x,x,label='linear')
exp.plot(x,x**2,label='quadratic')
exp.plot(x,x**3,label='cubic')
exp.xlabel('xlabel')
exp.ylabel('ylabel')
exp.title('Plot Simple')
exp.legend()

exp.show()
'''