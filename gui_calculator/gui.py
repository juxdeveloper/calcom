#import tkinter
#m = tkinter.Tk()
'''
widgets are added here
'''
#m.mainloop()
import tkinter as tk

# Texto
root = tk.Tk()
root.title('Título de la ventana')
root.geometry("800x450")
root.resizable(False, False)


ao = tk.Button(root, text='0', command=root.destroy)

a = tk.Button(root, text='1', command=root.destroy)
b = tk.Button(root, text='2', command=root.destroy)
c = tk.Button(root, text='3', command=root.destroy)

d = tk.Button(root, text='4', command=root.destroy)
e = tk.Button(root, text='5', command=root.destroy)
f = tk.Button(root, text='6', command=root.destroy)

g = tk.Button(root, text='7', command=root.destroy)
h = tk.Button(root, text='8', command=root.destroy)
i = tk.Button(root, text='9', command=root.destroy)


binomica = tk.Button(root, text='a+bi', command=root.destroy)
polar = tk.Button(root, text='r cis(°)', command=root.destroy)
exponencial = tk.Button(root, text='r e^iθπ', command=root.destroy)


potencia = tk.Button(root, text='x^n', command=root.destroy)
raiz = tk.Button(root, text='n√x', command=root.destroy)
multi = tk.Button(root, text='*', command=root.destroy)
divi = tk.Button(root, text='/', command=root.destroy)
suma = tk.Button(root, text='+', command=root.destroy)
resta = tk.Button(root, text='-', command=root.destroy)

borrar = tk.Button(root, text='<<-X|', command=root.destroy)

# .grid(row=y, column=x, columnspan=W)
# [filas, columnas, expansion columnas]
ao.grid(row=7,column=0)

a.grid(row=6,column=0)
b.grid(row=6,column=1)
c.grid(row=6,column=2, sticky='w')

d.grid(row=5,column=0)
e.grid(row=5,column=1)
f.grid(row=5,column=2, sticky='w')

g.grid(row=4,column=0)
h.grid(row=4,column=1)
i.grid(row=4,column=2, sticky='w')

binomica.grid(row=3,column=0, columnspan=2, sticky='we')
polar.grid(row=3,column=2, columnspan=2, sticky='we')
exponencial.grid(row=3,column=4, columnspan=2, sticky='we')


potencia.grid(row=7,column=4)
raiz.grid(row=7,column=5)
multi.grid(row=6,column=4, sticky='we')
divi.grid(row=6,column=5, sticky='we')
suma.grid(row=5,column=4, sticky='we')
resta.grid(row=5,column=5, sticky='we')

borrar.grid(row=4,column=4, columnspan=2, sticky='we')




operacion = tk.Label(root, text='+', bg="#07facd")
operacion.grid(row=2,column=0, sticky='we')


resultado = tk.Label(root, text='=4.08+4.8i', bg="#ff0000", anchor='e')
resultado.grid(row=2,column=1,columnspan=5, sticky='we')
root.mainloop()

