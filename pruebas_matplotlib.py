#instalar en arch sudo pacman -Syu python_matplotlib (o algo asi)
#en windows se instala con pip

import matplotlib.pyplot as plt #plt es el "canvas"
import numpy as np #numpy para hacer un array con un conjunto de valores a graficar

'''
PRUEBA1
POO

x=np.linspace(0,2,100) #desde dónde, hasta donde, cuántos valores entre el rango

fig, ax = plt.subplots(figsize=(10,6),layout='constrained')

ax.plot(x,x, label='lineal')
ax.plot(x,x**2, label='cuadrática')
ax.plot(x,x**3, label='cúbica')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.set_title('Plot Simple')
ax.legend()

plt.show()

pyplot
plt.figure(figsize=(15,7), layout='constrained')
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('Plot Simple')
plt.legend()

plt.show()
'''

'''
#PRUEBA2
datos_x = np.linspace(0,6,50)
datos_y = np.sin(datos_x)

#plt.plot(datos_x,datos_y,linewidth=3,linestyle=(0,(4,8,10,2))) 
#empieza en 0 a trazar, 4 espacios de linea, 8 de espacio, luego 10 de linea, 2 de espacio y repite el patron

#pyplot, no tiene tantas funciones como hacerlo en POO
#plt.stem(datos_x,datos_y, linefmt=('--''r'),markerfmt='D',basefmt='C5-.')

#POO
fig, ax = plt.subplots()
ax.stem(datos_x,datos_y, linefmt=('--''g'),markerfmt='D',basefmt='C5-.')

#Formato del cuadro de la grafica
ax.spines['left'].set_color('yellow')
ax.spines['left'].set_linewidth(7)
ax.spines['left'].set_alpha(0.5) #alpha es la transparencia, de 0 a 1
ax.spines['left'].set_linestyle('dashdot')
ax.spines['left'].set_capstyle('round') #redondea los bordes de las lineas
ax.spines['top'].set_visible(False)

ax.grid(axis='y',visible=True,linewidth=1.2,linestyle=(0,(8,2,10,4)),color='k') #color k es negro, wtf xd
ax.grid(axis='x',visible=True,linewidth=3.4,linestyle=(4,(12,4,3,9)),color='b')

plt.show()
'''

#PRUEBA3
r=np.linspace(0,2,20)
beta=2*np.pi*np.random.rand(20)
colors=beta

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
#crea una proyección polar

sc=ax.scatter(beta, r, c=r, s=100, cmap='hsv')
#angulo beta, distancia r, c es de color que va en funcion de r, la distancia al centro, s de size y color map hsv

fig.colorbar(mappable=sc,location='bottom')
plt.show()