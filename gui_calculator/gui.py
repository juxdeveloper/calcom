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
fbotonescalc = tk.Frame(
    root,
    bg="orange",
    bd=5,
    relief="solid"
)
for i in range(6):
    fbotonescalc.columnconfigure(i, uniform="group1")
fbotonescalc.grid(row=1, column=0, columnspan=6, sticky='wen')

tk.Button(fbotonescalc, text='0', command=lambda: enter("0")).grid(row=4, column=0, sticky='nswe') # Ajustado sticky para consistencia

tk.Button(fbotonescalc, text='1', command=lambda: enter("1")).grid(row=3,column=0, sticky='we')
tk.Button(fbotonescalc, text='2', command=lambda: enter("2")).grid(row=3,column=1, sticky='we')
tk.Button(fbotonescalc, text='3', command=lambda: enter("3")).grid(row=3,column=2, sticky='we')
tk.Button(fbotonescalc, text='4', command=lambda: enter("4")).grid(row=2,column=0, sticky='we')
tk.Button(fbotonescalc, text='5', command=lambda: enter("5")).grid(row=2,column=1, sticky='we')
tk.Button(fbotonescalc, text='6', command=lambda: enter("6")).grid(row=2,column=2, sticky='we')
tk.Button(fbotonescalc, text='7', command=lambda: enter("7")).grid(row=1,column=0, sticky='we')
tk.Button(fbotonescalc, text='8', command=lambda: enter("8")).grid(row=1,column=1, sticky='we')
tk.Button(fbotonescalc, text='9', command=lambda: enter("9")).grid(row=1,column=2, sticky='we')



####### BOTONES OPERACIONES @@@@@@@@@@@@



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
# Solo la columna 2 se expande. Las demás tienen ancho fijo.
frame.columnconfigure(2, weight=1)
frame.grid(row=0, column=0, padx=0, pady=0, columnspan=6, sticky='nwe')

# Widgets en columnas fijas 0 y 1
tk.Label(frame, text='z1', bg="#009F9F", width=3).grid(row=0,column=0, sticky='nswe')
lz1 = tk.Label(frame, text='binas', bg="#9F009F", width=9)
lz1.grid(row=0,column=1, sticky='nswe')

tk.Label(frame, text='z2', bg="#009F9F").grid(row=1,column=0, sticky='nswe')
lz2 = tk.Label(frame, text='pol', bg="#9F009F")
lz2.grid(row=1,column=1, sticky='nswe')

loperacion = tk.Label(frame, text='+', bg="#07facd")
loperacion.grid(row=5,column=0, sticky='we')




#tk.Spinbox(frame, from_=2, to=20, width=3).grid(row=5,column=2)
#tk.Label(frame, text='elevada a', bg="#ff9f94").grid(row=5,column=1, sticky='we')





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
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_binomicas.columnconfigure((0, 1), weight=1)
a1 = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd)
a1.grid(row=0, column=0, sticky='we')
b1 = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd)
b1.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas, text='i').grid(row=0, column=2)
#_binomicas.grid(row=0,column=2, columnspan=4, sticky='we')


_polares = tk.Frame(
    frame,
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_polares.columnconfigure((0, 2), weight=1)
rp1 = tk.Entry(_polares, validate='key', width=8, validatecommand=vcmd)
rp1.grid(row=0, column=0, sticky='we')
tk.Label(_polares, text='cis(').grid(row=0, column=1)
g1 = tk.Entry(_polares, validate='key', width=8,validatecommand=vcmd)
g1.grid(row=0, column=2, sticky='we')
tk.Label(_polares, text='°)').grid(row=0, column=3)


_exponenciales = tk.Frame(
    frame,
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_exponenciales.columnconfigure(0, weight=2)
_exponenciales.columnconfigure((2, 4), weight=1)

re1 = tk.Entry(_exponenciales, validate='key', width=8, validatecommand=vcmd)
re1.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales, text='e^i').grid(row=0, column=1)

t1_1 = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd)
t1_1.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales, text='/').grid(row=0, column=3)

t2_1 = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd)
t2_1.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales, text='π').grid(row=0, column=5)











_binomicas1 = tk.Frame(
    frame,
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_binomicas1.columnconfigure((0, 1), weight=1)
a2 = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd)
a2.grid(row=0, column=0, sticky='we')
b2 = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd)
b2.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas1, text='i').grid(row=0, column=2)
#_binomicas1.grid(row=0,column=2, columnspan=4, sticky='we')


_polares1 = tk.Frame(
    frame,
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_polares1.columnconfigure((0, 2), weight=1)
rp2 = tk.Entry(_polares1, validate='key', width=8, validatecommand=vcmd)
rp2.grid(row=0, column=0, sticky='we')
tk.Label(_polares1, text='cis(').grid(row=0, column=1)
g2 = tk.Entry(_polares1, validate='key', width=8,validatecommand=vcmd)
g2.grid(row=0, column=2, sticky='we')
tk.Label(_polares1, text='°)').grid(row=0, column=3)


_exponenciales1 = tk.Frame(
    frame,
    width=10,
    bg="lightgreen",
    bd=5,
    relief="solid"
)
_exponenciales1.columnconfigure(0, weight=2)
_exponenciales1.columnconfigure((2, 4), weight=1)

re2 = tk.Entry(_exponenciales1, validate='key', width=8, validatecommand=vcmd)
re2.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales1, text='e^i').grid(row=0, column=1)

t1_2 = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd)
t1_2.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales1, text='/').grid(row=0, column=3)

t2_2 = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd)
t2_2.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales1, text='π').grid(row=0, column=5)











#_exponenciales.grid(row=1,column=2, columnspan=4, sticky='we')

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
tk.Label(right_frame, text='Operaciones', bg="#ff0000", anchor='w').grid(row=0,column=0, sticky='we')

fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 
ax.plot([1, 9, 3], [4, 5, 6])

canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana
canvas.get_tk_widget().grid(row=1,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")




# GRÁFICA 2 ==================================================================
tk.Label(right_frame, text='Resultado', bg="#ff0000", anchor='w').grid(row=3,column=0, sticky='we')

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






tipo1 = 0
tipo2 = 0
coperacion = 0









def opera_n(tipo):
    global state
    state = 1
    nspin.grid_forget()
    ntext.grid_forget()
    nspin.grid(row=5,column=2, sticky='w')
    ntext.grid(row=5,column=1, sticky='we')
    global coperacion
    match tipo:
        case 1:
            loperacion.config(text='^')
            ntext.config(text='elevado a ')
            coperacion = 5
        case 2:
            loperacion.config(text='√')
            ntext.config(text='de índice')
            coperacion = 6

# 2. Operaciones
potencia = tk.Button(fbotonescalc, text='x^n', state=tk.DISABLED, command=lambda: opera_n(1))
potencia.grid(row=4,column=4)
raiz = tk.Button(fbotonescalc, text='n√x', state=tk.DISABLED, command=lambda: opera_n(2))
raiz.grid(row=4,column=5)





def opera(tipo):
    global state
    state = 1
    nspin.grid_forget()
    ntext.grid_forget()
    global coperacion
    match tipo:
        case 1:
            loperacion.config(text='+')
            coperacion = 1
        case 2:
            loperacion.config(text='-')
            coperacion = 2
        case 3:
            loperacion.config(text='*')
            coperacion = 3
        case 4:
            loperacion.config(text='/')
            coperacion = 4

suma = tk.Button(fbotonescalc, text='+', state=tk.DISABLED, command=lambda: opera(1))
suma.grid(row=2,column=4, sticky='we')
resta = tk.Button(fbotonescalc, text='-', state=tk.DISABLED, command=lambda: opera(2))
resta.grid(row=2,column=5, sticky='we')
multi = tk.Button(fbotonescalc, text='*', state=tk.DISABLED, command=lambda: opera(3))
multi.grid(row=3,column=4, sticky='we')
divi = tk.Button(fbotonescalc, text='/', state=tk.DISABLED, command=lambda: opera(4))
divi.grid(row=3,column=5, sticky='we')










state = 0
stateOP = 0
def corre(tipo, state):
    global stateOP
    if stateOP == 0:
        suma.config(state=tk.NORMAL)
        resta.config(state=tk.NORMAL)
        divi.config(state=tk.NORMAL)
        multi.config(state=tk.NORMAL)
        potencia.config(state=tk.NORMAL)
        raiz.config(state=tk.NORMAL)
    stateOP = 1
    if state == 0:
        _binomicas.grid_forget()
        _polares.grid_forget()
        _exponenciales.grid_forget()
        global tipo1
        tipo1 = tipo
        match tipo:
            case 1:
                lz1.config(text="bin")
                _binomicas.grid(row=0, column=2, sticky='nsew')
            case 2:
                lz1.config(text="pol")
                _polares.grid(row=0, column=2, sticky='nsew')
            case 3:
                lz1.config(text="exp")
                _exponenciales.grid(row=0, column=2, sticky='nsew')
    else:
        _binomicas1.grid_forget()
        _polares1.grid_forget()
        _exponenciales1.grid_forget()
        global tipo2
        tipo2 = tipo
        match tipo:
            case 1:
                lz2.config(text="bin")
                _binomicas1.grid(row=1, column=2, sticky='nsew')
            case 2:
                lz2.config(text="pol")
                _polares1.grid(row=1, column=2, sticky='nsew')
            case 3:
                lz2.config(text="exp")
                _exponenciales1.grid(row=1, column=2, sticky='nsew')
    #binomica.config(state=tk.DISABLED)
    #polar.config(state=tk.DISABLED)
    #exponencial.config(state=tk.DISABLED)


# 1. Botones para seleccionar el tipo

binomica = tk.Button(fbotonescalc, text='a+bi', command=lambda: corre(1, state), width=5)
binomica.grid(row=0,column=0, columnspan=2, sticky='we')
polar = tk.Button(fbotonescalc, text='r cis(°)', command=lambda: corre(2, state), width=5)
polar.grid(row=0,column=2, columnspan=2, sticky='we')
exponencial = tk.Button(fbotonescalc, text='r e^iθπ', command=lambda: corre(3, state), width=5)
exponencial.grid(row=0,column=4, columnspan=2, sticky='we')





nspin = tk.Spinbox(frame, from_=2, to=20, width=3)
ntext = tk.Label(frame, text='', bg="#ff9f94", width=4)
borrar = tk.Button(fbotonescalc, text='⌫', command=lambda: deletee())
borrar.grid(row=1,column=4, columnspan=2, sticky='we')









lresultado = tk.Label(frame, text='=', bg="#ff0000", anchor='e')
lresultado.grid(row=5,column=1,columnspan=5, sticky='we')



def computar(tipo1, tipo2, operacion):
    print("tipo1: " + str(tipo1))
    print("tipo2: " + str(tipo2))
    print("operacion: " + str(operacion))
    lresultado.config(text='resultado pro')

# 3. Resultado

equal = tk.Button(fbotonescalc, text='=', command=lambda: computar(tipo1,tipo2,coperacion)).grid(row=4, column=1, columnspan=2, sticky='nswe')

root.mainloop()