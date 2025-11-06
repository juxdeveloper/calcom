import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 1. BOTÓN Pon el primer tipo de número
#       Muestra tipo
#       Muestra form
#       Maneja entrada
#       Actualiza gráfico
# 2. Tecla ENTER
#       Valida entrada

# 3. Selecciona operador

# 4. BOTÓN Pon el primer tipo de número
#       Muestra tipo
#       Muestra form
#       Maneja entrada
#       Actualiza gráfico
# 5. Tecla ENTER
#       Valida entrada

root = tk.Tk()
root.title('calcom')
#root.geometry("800x450")
root.resizable(False, False)
root.rowconfigure(2, weight=1)


###########################################################################
# FRAME 1
###########################################################################
button_frame = tk.Frame(
    root,
    bg="orange",
    bd=5,
    relief="solid"
)

for i in range(6):
    button_frame.columnconfigure(i, uniform="group1")
button_frame.grid(row=1, column=0, padx=0, pady=0, columnspan=6, sticky='wen')


ao = tk.Button(button_frame, text='0', command=lambda: enter("0"))
ae = tk.Button(button_frame, text='=', command=lambda: enter("="))
a = tk.Button(button_frame, text='1', command=lambda: enter("1"))
b = tk.Button(button_frame, text='2', command=lambda: enter("2"))
c = tk.Button(button_frame, text='3', command=lambda: enter("3"))
d = tk.Button(button_frame, text='4', command=lambda: enter("4"))
e = tk.Button(button_frame, text='5', command=lambda: enter("5"))
f = tk.Button(button_frame, text='6', command=lambda: enter("6"))
g = tk.Button(button_frame, text='7', command=lambda: enter("7"))
h = tk.Button(button_frame, text='8', command=lambda: enter("8"))
i = tk.Button(button_frame, text='9', command=lambda: enter("9"))
binomica = tk.Button(button_frame, text='a+bi', command=root.destroy, width=5)
polar = tk.Button(button_frame, text='r cis(°)', command=root.destroy, width=5)
exponencial = tk.Button(button_frame, text='r e^iθπ', command=root.destroy, width=5)
potencia = tk.Button(button_frame, text='x^n', command=lambda: enter("1"))
raiz = tk.Button(button_frame, text='n√x', command=lambda: enter("1"))
multi = tk.Button(button_frame, text='*', command=lambda: enter("1"))
divi = tk.Button(button_frame, text='/', command=lambda: enter("1"))
suma = tk.Button(button_frame, text='+', command=lambda: enter("1"))
resta = tk.Button(button_frame, text='-', command=lambda: enter("1"))
borrar = tk.Button(button_frame, text='⌫', command=lambda: deletee())


ae.grid(row=4, column=1, columnspan=2, sticky='nswe') # Quitado columnspan y ajustado sticky
ao.grid(row=4, column=0, sticky='nswe') # Ajustado sticky para consistencia
a.grid(row=3,column=0, sticky='we')
b.grid(row=3,column=1, sticky='we')
c.grid(row=3,column=2, sticky='we')
d.grid(row=2,column=0, sticky='we')
e.grid(row=2,column=1, sticky='we')
f.grid(row=2,column=2, sticky='we')
g.grid(row=1,column=0, sticky='we')
h.grid(row=1,column=1, sticky='we')
i.grid(row=1,column=2, sticky='we')
binomica.grid(row=0,column=0, columnspan=2, sticky='we')
polar.grid(row=0,column=2, columnspan=2, sticky='we')
exponencial.grid(row=0,column=4, columnspan=2, sticky='we')
potencia.grid(row=4,column=4)
raiz.grid(row=4,column=5)
multi.grid(row=3,column=4, sticky='we')
divi.grid(row=3,column=5, sticky='we')
suma.grid(row=2,column=4, sticky='we')
resta.grid(row=2,column=5, sticky='we')
borrar.grid(row=1,column=4, columnspan=2, sticky='we')




###########################################################################
# FRAME 2
###########################################################################
frame = tk.Frame(
    root,
    bg="yellow",
    bd=5,
    relief="solid",   # solid border
    highlightbackground="black",  # border color
    highlightthickness=0.5
)
frame.columnconfigure(1,weight=1)
frame.columnconfigure(5,weight=2)
frame.grid(row=0, column=0, padx=0, pady=0, columnspan=6, sticky='nwe')


t1 = tk.Label(frame, text='z1', bg="#009F9F")
t1.grid(row=0,column=0, sticky='nswe')
tr1 = tk.Label(frame, text='bin', bg="#9F009F")
tr1.grid(row=0,column=1, columnspan=2, sticky='nswe')

t1 = tk.Label(frame, text='z2', bg="#009F9F")
t1.grid(row=1,column=0, sticky='nswe')
tr1 = tk.Label(frame, text='pol', bg="#9F009F")
tr1.grid(row=1,column=1, sticky='nswe')

operacion = tk.Label(frame, text='+', bg="#07facd")
operacion.grid(row=5,column=0, sticky='we')

resultado = tk.Label(frame, text='=4.08+4.8i', bg="#ff0000", anchor='e')
resultado.grid(row=5,column=1,columnspan=5, sticky='we')

def enter(string):
    w = root.focus_get()
    if isinstance(w, tk.Entry):
        w.insert(tk.END, string)

def deletee():
    w = root.focus_get()
    if isinstance(w, tk.Entry):
        w.delete(len(w.get())-1, tk.END)

def validate(P):
    try:
        float(P)
        return True
    except ValueError:
        return P == "" or P == "-" or P == "+"
vcmd = (frame.register(validate), '%P')



# INPUT HANDLE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
_binomicas = tk.Frame(
    frame,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd).pack(side=tk.LEFT)# grid(row=0,column=0, sticky='we')
tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd).pack(side=tk.LEFT)# grid(row=0,column=1, sticky='we')
tk.Label(_binomicas, text='i').pack(side=tk.LEFT,fill=tk.BOTH, expand=True) #grid(row=0,column=2, sticky='we')
_binomicas.grid(row=0,column=2, columnspan=4, sticky='we')
#lz1.grid(row=0,column=2, columnspan=4, sticky='we')


_polares = tk.Frame(
    frame,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
tk.Entry(_polares, validate='key', width=8, validatecommand=vcmd).pack(side=tk.LEFT)
tk.Label(_polares, text='cis(').pack(side=tk.LEFT)
tk.Entry(_polares, validate='key', width=8,validatecommand=vcmd).pack(side=tk.LEFT)
tk.Label(_polares, text='°)').pack(fill=tk.BOTH, expand=True)
#_polares.grid(row=1,column=2, columnspan=4, sticky='we')



_exponenciales = tk.Frame(
    frame,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
tk.Entry(_exponenciales, validate='key', width=8, validatecommand=vcmd).pack(side=tk.LEFT)
tk.Label(_exponenciales, text='e^i').pack(side=tk.LEFT)
tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd).pack(side=tk.LEFT)
tk.Label(_exponenciales, text='/').pack(side=tk.LEFT)
tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd).pack(side=tk.LEFT)
tk.Label(_exponenciales, text='π').pack(fill=tk.BOTH, expand=True)
_exponenciales.grid(row=1,column=2, columnspan=4, sticky='we')

tk.Button(root, text="HALT", command=root.destroy).grid(row=8,column=0)





###########################################################################
# FRAME 3
###########################################################################
right_frame = tk.Frame(
    root,
    bg="lightblue",
    bd=5,
    relief="solid"
)
right_frame.grid(row=0, column=6, rowspan=8, sticky='nswe', padx=0, pady=0)



# GRÁFICA 1 ==================================================================
resultado = tk.Label(right_frame, text='Operaciones', bg="#ff0000", anchor='w')
resultado.grid(row=0,column=0, sticky='we')

fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 
ax.plot([1, 9, 3], [4, 5, 6])

canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana
canvas.get_tk_widget().grid(row=1,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")




# GRÁFICA 2 ==================================================================
resultado = tk.Label(right_frame, text='Resultado', bg="#ff0000", anchor='w')
resultado.grid(row=3,column=0, sticky='we')

fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 
ax.plot([1, 2, 3], [4, 5, 6])

canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana
canvas.get_tk_widget().grid(row=4,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")


# MENU ==================================================================
info = tk.Button(root, text='(i)', command=lambda: enter("1"))
info.grid(row=0,column=7, sticky='wen')

info = tk.Button(root, text='⏾', command=lambda: enter("1"))
info.grid(row=0,column=8, sticky='wen')
root.mainloop()