#import tkinter
#m = tkinter.Tk()
'''
widgets are added here
'''
#m.mainloop()
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Texto
root = tk.Tk()
root.title('Título de la ventana')
root.geometry("800x450")
root.resizable(False, False)

# AÑADIDO: CONFIGURAMOS LA REJILLA PARA QUE LA COLUMNA 6 (DEL GRÁFICO) SE EXPANDA
#root.columnconfigure(6, weight=1)
# AÑADIDO: CONFIGURAMOS LAS FILAS PARA QUE SE PUEDAN EXPANDIR VERTICALMENTE
#root.rowconfigure(0, weight=1)


button_frame = tk.Frame(
    root,
    bg="orange",
    bd=5,
    relief="solid"
)

#frame.columnconfigure(1, weight=1)
button_frame.grid(row=1, column=0, padx=0, pady=0, columnspan=6, sticky='wes')


ao = tk.Button(button_frame, text='0', command=root.destroy)

a = tk.Button(button_frame, text='1', command=root.destroy)
b = tk.Button(button_frame, text='2', command=root.destroy)
c = tk.Button(button_frame, text='3', command=root.destroy)

d = tk.Button(button_frame, text='4', command=root.destroy)
e = tk.Button(button_frame, text='5', command=root.destroy)
f = tk.Button(button_frame, text='6', command=root.destroy)

g = tk.Button(button_frame, text='7', command=root.destroy)
h = tk.Button(button_frame, text='8', command=root.destroy)
i = tk.Button(button_frame, text='9', command=root.destroy)


binomica = tk.Button(button_frame, text='a+bi', command=root.destroy)
polar = tk.Button(button_frame, text='r cis(°)', command=root.destroy)
exponencial = tk.Button(button_frame, text='r e^iθπ', command=root.destroy)


potencia = tk.Button(button_frame, text='x^n', command=root.destroy)
raiz = tk.Button(button_frame, text='n√x', command=root.destroy)
multi = tk.Button(button_frame, text='*', command=root.destroy)
divi = tk.Button(button_frame, text='/', command=root.destroy)
suma = tk.Button(button_frame, text='+', command=root.destroy)
resta = tk.Button(button_frame, text='-', command=root.destroy)

borrar = tk.Button(button_frame, text='<<-X|', command=root.destroy)

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







frame = tk.Frame(
    root,
    bg="yellow",
    bd=5,
    relief="solid",   # solid border
    highlightbackground="black",  # border color
    highlightthickness=0.5
)
# Place the frame at row=0, col=0
frame.columnconfigure(1, weight=1)
frame.grid(row=0, column=0, padx=0, pady=0, columnspan=6, sticky='wes')




t1 = tk.Label(frame, text='z1', bg="#009F9F", anchor='e')
t1.grid(row=0,column=0,columnspan=1, sticky='we')

tr1 = tk.Label(frame, text='bin', bg="#9F009F")
tr1.grid(row=0,column=1,columnspan=1, sticky='we')

lz1 = tk.Label(frame, text='3+2i', bg="#00ff00", anchor='e')
lz1.grid(row=0,column=2,columnspan=4, sticky='we')




t2 = tk.Label(frame, text='z2', bg="#009F9F", anchor='e')
t2.grid(row=1,column=0,columnspan=1, sticky='we')

tr2 = tk.Label(frame, text='pol', bg="#9F009F")
tr2.grid(row=1,column=1,columnspan=1, sticky='we')

lz2 = tk.Label(frame, text='3cis(69°)', bg="#00ff00", anchor='e')
lz2.grid(row=1,column=2,columnspan=4, sticky='we')




operacion = tk.Label(frame, text='+', bg="#07facd")
operacion.grid(row=2,column=0, sticky='we')

resultado = tk.Label(frame, text='=4.08+4.8i', bg="#ff0000", anchor='e')
resultado.grid(row=2,column=1,columnspan=5, sticky='we')













# --- New frame to the right of the yellow one ---
right_frame = tk.Frame(
    root,
    bg="lightblue",
    bd=5,
    relief="solid"
)

# Place it at the same row, but one column to the right (col 6)
right_frame.grid(row=0, column=6, rowspan=8, sticky='nswe', padx=0, pady=0)

# Example content inside the right frame
right_label = tk.Label(right_frame, text="New Frame", bg="lightblue")

# Optional: expand both sides
root.columnconfigure(6, weight=1)
root.rowconfigure(0, weight=1)






resultado = tk.Label(right_frame, text='Por operar', bg="#ff0000", anchor='w')
resultado.grid(row=0,column=0, sticky='we')


fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 

# 3. Dibujar en la figura (usando tu código)
ax.plot([1, 2, 3], [4, 5, 6])

# 4. Crear el widget que une Matplotlib con Tkinter
canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana

# 5. Colocar el widget en la ventana de Tkinter
# MODIFICADO: EL GRÁFICO AHORA EMPIEZA EN LA FILA 0 Y SE EXPANDE 8 FILAS PARA CUBRIR TODO EL ALTO
canvas.get_tk_widget().grid(row=1,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")






resultado = tk.Label(right_frame, text='Resultado', bg="#ff0000", anchor='w')
resultado.grid(row=3,column=0, sticky='we')


fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 

# 3. Dibujar en la figura (usando tu código)
ax.plot([1, 2, 3], [4, 5, 6])

# 4. Crear el widget que une Matplotlib con Tkinter
canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana

# 5. Colocar el widget en la ventana de Tkinter
# MODIFICADO: EL GRÁFICO AHORA EMPIEZA EN LA FILA 0 Y SE EXPANDE 8 FILAS PARA CUBRIR TODO EL ALTO
canvas.get_tk_widget().grid(row=4,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")














#resultado = tk.Label(root, text='=4.08+4.8i', bg="#ff0000", anchor='e')
info = tk.Button(root, text='(i)', command=root.destroy)
info.grid(row=0,column=7, sticky='wen')

info = tk.Button(root, text='⏾', command=root.destroy)
info.grid(row=0,column=8, sticky='wen')
root.mainloop()