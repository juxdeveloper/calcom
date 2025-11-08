import tkinter as tk
from PIL import Image, ImageTk
import operations
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import matplotlib.pyplot as plt
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
root.configure(bg='white')
root.rowconfigure(2, weight=1)



# {'family': 'Noto Sans', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}

#default_font_object = font.nametofont("TkDefaultFont")
#default_font_details = default_font_object.actual()
#print(default_font_details)


###########################################################################
# FRAME 1
###########################################################################
fbotonescalc = tk.Frame(
    root,
    bg="white",
    bd=5,
    relief="flat"
)
for i in range(6):
    fbotonescalc.columnconfigure(i, uniform="group1")
fbotonescalc.grid(row=1, column=0, columnspan=6, sticky='wen')

tk.Button(fbotonescalc,relief="flat", bg="#FAFEE1", text='0', highlightthickness=0, command=lambda: enter("0")).grid(row=4, column=0, sticky='nswe') # Ajustado sticky para consistencia
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='1', highlightthickness=0, command=lambda: enter("1")).grid(row=3,column=0, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='2', highlightthickness=0, command=lambda: enter("2")).grid(row=3,column=1, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='3', highlightthickness=0, command=lambda: enter("3")).grid(row=3,column=2, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='4', highlightthickness=0, command=lambda: enter("4")).grid(row=2,column=0, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='5', highlightthickness=0, command=lambda: enter("5")).grid(row=2,column=1, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='6', highlightthickness=0, command=lambda: enter("6")).grid(row=2,column=2, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='7', highlightthickness=0, command=lambda: enter("7")).grid(row=1,column=0, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='8', highlightthickness=0, command=lambda: enter("8")).grid(row=1,column=1, sticky='we')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='9', highlightthickness=0, command=lambda: enter("9")).grid(row=1,column=2, sticky='we')



####### BOTONES OPERACIONES @@@@@@@@@@@@



###########################################################################
# FRAME 2
###########################################################################
frame = tk.Frame(
    root,
    bg="white",
    bd=5,
    relief="solid",   # solid border
    #highlightbackground="black",  # border color
    #highlightthickness=0.5
)
# Solo la columna 2 se expande. Las demás tienen ancho fijo.
frame.columnconfigure(2, weight=1)
frame.grid(row=0, column=0, padx=0, pady=0, columnspan=6, sticky='nwe')

# Widgets en columnas fijas 0 y 1
tk.Label(frame, text='z1', bg="#009F9F", width=3).grid(row=0,column=0, sticky='nswe')
lz1 = tk.Label(frame, text='forma', bg="#FAFEE1", width=9)
lz1.grid(row=0,column=1, sticky='nswe')

tk.Label(frame, text='z2', bg="#009F9F").grid(row=1,column=0, sticky='nswe')
lz2 = tk.Label(frame, text='forma', bg="#FAFEE1")
lz2.grid(row=1,column=1, sticky='nswe')







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
# Frame para Forma Binómica
_binomicas = tk.Frame(
    frame,
    width=10,
    relief="solid",
)
_binomicas.columnconfigure((0, 1), weight=1)
# Nombres únicos para los Entry de z1 binómico
entry_bin1_real = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin1_real.grid(row=0, column=0, sticky='we')
entry_bin1_imag = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin1_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas, text='i', bg="#DBFEEF").grid(row=0, column=2, sticky="ns")

# Frame para Forma Polar
_polares = tk.Frame(
    frame,
    width=10,
    relief="solid"
)
_polares.columnconfigure((0, 2), weight=1)
# Nombres únicos para los Entry de z1 polar
entry_pol1_mod = tk.Entry(_polares, validate='key', width=8, validatecommand=vcmd, relief="flat",  highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol1_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares, text='cis(', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_pol1_arg = tk.Entry(_polares, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol1_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares, text='°)', bg="#DBFEEF").grid(row=0, column=3, sticky="ns")

# Frame para Forma Exponencial
_exponenciales = tk.Frame(
    frame,
    width=10,
    relief="solid"
)
_exponenciales.columnconfigure(0, weight=2)
_exponenciales.columnconfigure((2, 4), weight=1)
# Nombres únicos para los Entry de z1 exponencial
entry_exp1_mod = tk.Entry(_exponenciales, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp1_mod.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales, text='e^i', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_exp1_num = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp1_num.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales, text='/', bg="#DBFEEF").grid(row=0, column=3, sticky='ns')
entry_exp1_den = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp1_den.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales, text='π', bg="#DBFEEF").grid(row=0, column=5, sticky='ns')


# --- WIDGETS PARA EL SEGUNDO NÚMERO (z2) ---

# Frame para Forma Binómica 2
_binomicas1 = tk.Frame(
    frame,
    width=10,
    relief="solid"
)
_binomicas1.columnconfigure((0, 1), weight=1)
# Nombres únicos para los Entry de z2 binómico
entry_bin2_real = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin2_real.grid(row=0, column=0, sticky='we')
entry_bin2_imag = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin2_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas1, text='i', bg="#DBFEEF").grid(row=0, column=2, sticky='ns')

# Frame para Forma Polar 2
_polares1 = tk.Frame(
    frame,
    width=10,
    relief="solid"
)
_polares1.columnconfigure((0, 2), weight=1)
# Nombres únicos para los Entry de z2 polar
entry_pol2_mod = tk.Entry(_polares1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares1, text='cis(', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_pol2_arg = tk.Entry(_polares1, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol2_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares1, text='°)', bg="#DBFEEF").grid(row=0, column=3, sticky='ns')

# Frame para Forma Exponencial 2
_exponenciales1 = tk.Frame(
    frame,
    width=10,
    relief="solid"
)
_exponenciales1.columnconfigure(0, weight=2)
_exponenciales1.columnconfigure((2, 4), weight=1)
# Nombres únicos para los Entry de z2 exponencial
entry_exp2_mod = tk.Entry(_exponenciales1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales1, text='e^i', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_exp2_num = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_num.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales1, text='/', bg="#DBFEEF").grid(row=0, column=3, sticky='ns')
entry_exp2_den = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_den.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales1, text='π', bg="#DBFEEF").grid(row=0, column=5, sticky='ns')











#_exponenciales.grid(row=1,column=2, columnspan=4, sticky='we')





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
tk.Label(right_frame, text='Operaciones', bg="white", anchor='w').grid(row=0,column=0, sticky='we')

fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 
ax.plot([1, 2, 3], [4, 5, 6])

canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana
canvas.get_tk_widget().grid(row=1,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")



# GRÁFICA 2 ==================================================================
tk.Label(right_frame, text='Resultado', bg="white", anchor='w').grid(row=3,column=0, sticky='we')

fig = Figure(figsize=(3, 2), dpi=96)
ax = fig.add_subplot(111) 
ax.plot([1, 2, 3], [4, 5, 6])

canvas = FigureCanvasTkAgg(fig, master=right_frame)  # 'fig' es nuestro gráfico, 'root' es la ventana
canvas.get_tk_widget().grid(row=4,column=0, rowspan=2, sticky='we') # grid(row=2,column=6, rowspan=1, sticky="e")


# MENU ==================================================================
def info_window():
    new_window = tk.Toplevel(root)
    new_window.title("Información")
    new_window.geometry("300x450")

    image = Image.open('logo.png').resize((50, 50))
    photo_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(new_window, image=photo_image)
    image_label.image = photo_image # Para el recolector de basura
    image_label.pack()

    tk.Label(new_window, text="calcom GUI").pack(pady=10) 
    tk.Label(new_window, text="fornite").pack()

theme = tk.Button(root, text='🛈', command=info_window, bg="#0A4F6D", fg="white", relief="flat", highlightthickness=0)
theme.grid(row=0,column=7, sticky='wen')

stheme = 0
def chtheme():
    global stheme
    if stheme == 0:
        theme.config(text="☀︎")
        root.configure(bg='#1a1a1a')
        frame.configure(bg='#1a1a1a')
        fbotonescalc.configure(bg='#1a1a1a')
        stheme = 1
    elif stheme == 1:
        theme.config(text="❨")
        root.configure(bg='white')
        frame.configure(bg='white')
        fbotonescalc.configure(bg='white')
        stheme = 0


theme = tk.Button(root, text='❨', command=lambda: chtheme(), bg="#0A4F6D", fg="white", relief="flat", highlightthickness=0)
theme.grid(row=0,column=8, sticky='wen')
close = tk.Button(root, text='⨯', command=root.destroy, bg="#6C100A", fg="white", relief="flat", highlightthickness=0)
close.grid(row=0,column=9, sticky='wen')



tipo1 = 0
tipo2 = 0
coperacion = 0









def opera_n(tipo):
    global state
    state = 1
    ntext.grid_forget()
    nspin.grid_forget()
    lresultado.grid_forget()
    ntext.grid(row=0, column=1, sticky='e')
    nspin.grid(row=0, column=2)
    lresultado.grid(row=0, column=3, columnspan=1, sticky='we')
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
potencia = tk.Button(fbotonescalc, text='x^n',  relief="flat", highlightthickness=0, bg="#84D0FD", fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(1))
potencia.grid(row=4,column=4)
raiz = tk.Button(fbotonescalc, text='n√x',  relief="flat", highlightthickness=0, bg="#84D0FD", fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(2))
raiz.grid(row=4,column=5)





# FRAME OPERACIONES
operation_row_frame = tk.Frame(frame, bg="yellow") # Mismo color para que sea invisible
operation_row_frame.grid(row=5, column=0, columnspan=6, sticky='we')
operation_row_frame.columnconfigure(3, weight=1)





def opera(tipo):
    global state
    state = 1
    nspin.grid_forget()
    ntext.grid_forget()
    lresultado.grid_forget()
    lresultado.grid(row=0, column=1, columnspan=3, sticky='we')
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

suma = tk.Button(fbotonescalc, text='+', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(1))
suma.grid(row=2,column=4, sticky='we')
resta = tk.Button(fbotonescalc, text='-', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(2))
resta.grid(row=2,column=5, sticky='we')
multi = tk.Button(fbotonescalc, text='*', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(3))
multi.grid(row=3,column=4, sticky='we')
divi = tk.Button(fbotonescalc, text='/', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(4))
divi.grid(row=3,column=5, sticky='we')










state = 0
stateOP = 0
def corre(tipo, state):


    ############
    ############
    ############

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

binomica = tk.Button(fbotonescalc, text='a+bi', command=lambda: corre(1, state), width=5, bg="#0A4F6D", fg="white", relief="flat", highlightthickness=0)
binomica.grid(row=0,column=0, columnspan=2, sticky='we')
polar = tk.Button(fbotonescalc, text='r cis(°)', command=lambda: corre(2, state), width=5, bg="#0A4F6D", fg="white", relief="flat", highlightthickness=0)
polar.grid(row=0,column=2, columnspan=2, sticky='we')
exponencial = tk.Button(fbotonescalc, text='r e^iθπ', command=lambda: corre(3, state), width=5, bg="#0A4F6D", fg="white", relief="flat", highlightthickness=0)
exponencial.grid(row=0,column=4, columnspan=2, sticky='we')





nspin = tk.Spinbox(frame, from_=2, to=20, width=3)
ntext = tk.Label(frame, text='', bg="#ff9f94", width=4)
borrar = tk.Button(fbotonescalc, text='⌫', command=lambda: deletee(), bg="#6C100A", fg="white", highlightthickness=0, relief="flat")
borrar.grid(row=1,column=4, columnspan=2, sticky='we')












loperacion = tk.Label(operation_row_frame, text='op', width=3, bg="#84D0FD")
ntext = tk.Label(operation_row_frame, text='', bg="#ff9f94")
nspin = tk.Spinbox(operation_row_frame, from_=2, to=20, width=3)
lresultado = tk.Label(operation_row_frame, text='=', anchor='e', bg="#0A4F6D", fg="white")

loperacion.grid(row=0, column=0, sticky='we')
lresultado.grid(row=0, column=1, columnspan=3, sticky='we')





def computar(tipo1, tipo2, operacion):
    # --- 1. Obtener valores del primer número (z1) ---
    v1, v2 = 0.0, 0.0
    if tipo1 == 1: # Binómica
        v1 = float(entry_bin1_real.get())
        v2 = float(entry_bin1_imag.get())
    elif tipo1 == 2: # Polar
        v1 = float(entry_pol1_mod.get())
        v2 = float(entry_pol1_arg.get())
    elif tipo1 == 3: # Exponencial
        v1 = float(entry_exp1_mod.get())
        v2 = float(entry_exp1_num.get()) / float(entry_exp1_den.get())

    # --- 2. Obtener valores del segundo número (z2), si es necesario ---
    v3, v4 = 0.0, 0.0
    # Solo se necesita un segundo número para las 4 operaciones básicas
    if operacion <= 4:
        if tipo2 == 1: # Binómica
            v3 = float(entry_bin2_real.get())
            v4 = float(entry_bin2_imag.get())
        elif tipo2 == 2: # Polar
            v3 = float(entry_pol2_mod.get())
            v4 = float(entry_pol2_arg.get())
        elif tipo2 == 3: # Exponencial
            v3 = float(entry_exp2_mod.get())
            v4 = float(entry_exp2_num.get()) / float(entry_exp2_den.get())

    # --- 3. Realizar el cálculo ---
    resultado = ""
    string = ""
    match operacion:
        case 1: # Suma
            resultado = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, 0)
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}{"+" if resultado[1]>=0 else "-"}{f'{abs(resultado[1]):.4f}'.rstrip('0').rstrip('.')}i"
        case 2: # Resta
            resultado = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, 1)
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}{"+" if resultado[1]>=0 else "-"}{f'{abs(resultado[1]):.4f}'.rstrip('0').rstrip('.')}i"
        case 3: # Multiplicación
            resultado = operations.factor(tipo1, v1, v2, tipo2, v3, v4, 0)
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}cis({f'{resultado[1]:.4f}'.rstrip('0').rstrip('.')}°)"
        case 4: # División
            resultado = operations.factor(tipo1, v1, v2, tipo2, v3, v4, 1)
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}cis({f'{resultado[1]:.4f}'.rstrip('0').rstrip('.')}°)"
        case 5: # Potencia
            n = int(nspin.get())
            resultado = operations.potencia(tipo1, v1, v2, n, 0) # Asumo que 'n' es el exponente
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}cis({f'{resultado[1]:.4f}'.rstrip('0').rstrip('.')}°)"
        case 6: # Raíz
            n = int(nspin.get())
            resultado = operations.potencia(tipo1, v1, v2, n, 1) # Asumo que 'n' es el índice de la raíz
            string = f"{f'{resultado[0]:.4f}'.rstrip('0').rstrip('.')}cis({f'{resultado[1]:.4f}'.rstrip('0').rstrip('.')}°)"

    # --- 4. Mostrar el resultado ---
    lresultado.config(text=f"= {string}")

# 3. Resultado

equal = tk.Button(fbotonescalc, text='=', command=lambda: computar(tipo1,tipo2,coperacion), bg="#0A4F6D",  highlightthickness=0, fg="white", relief="flat").grid(row=4, column=1, columnspan=2, sticky='nswe')

root.mainloop()