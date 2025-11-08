import customtkinter as ctk
import tkinter as tk  # Kept for the Spinbox widget
import operations
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Set the appearance and theme for customtkinter
ctk.set_appearance_mode("System")  # Can be "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Can be "blue", "green", "dark-blue"

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

root = ctk.CTk()
root.title('calcom')
#root.geometry("800x450")
root.resizable(False, False)
root.rowconfigure(2, weight=1)


###########################################################################
# FRAME 1
###########################################################################
fbotonescalc = ctk.CTkFrame(
    root,
    fg_color="transparent", # Replaces bg, bd, relief
    border_width=2
)
for i in range(6):
    fbotonescalc.columnconfigure(i, uniform="group1")
fbotonescalc.grid(row=1, column=0, columnspan=6, sticky='wen', padx=5, pady=5)

ctk.CTkButton(fbotonescalc, text='0', command=lambda: enter("0")).grid(row=4, column=0, sticky='nswe', padx=2, pady=2)

ctk.CTkButton(fbotonescalc, text='1', command=lambda: enter("1")).grid(row=3,column=0, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='2', command=lambda: enter("2")).grid(row=3,column=1, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='3', command=lambda: enter("3")).grid(row=3,column=2, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='4', command=lambda: enter("4")).grid(row=2,column=0, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='5', command=lambda: enter("5")).grid(row=2,column=1, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='6', command=lambda: enter("6")).grid(row=2,column=2, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='7', command=lambda: enter("7")).grid(row=1,column=0, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='8', command=lambda: enter("8")).grid(row=1,column=1, sticky='we', padx=2, pady=2)
ctk.CTkButton(fbotonescalc, text='9', command=lambda: enter("9")).grid(row=1,column=2, sticky='we', padx=2, pady=2)

####### BOTONES OPERACIONES @@@@@@@@@@@@

###########################################################################
# FRAME 2
###########################################################################
frame = ctk.CTkFrame(
    root,
    fg_color="transparent" # Removed bg, bd, relief, highlightbackground, highlightthickness
)
# Solo la columna 2 se expande. Las demás tienen ancho fijo.
frame.columnconfigure(2, weight=1)
frame.grid(row=0, column=0, padx=5, pady=5, columnspan=6, sticky='nwe')

# Widgets en columnas fijas 0 y 1
ctk.CTkLabel(frame, text='z1', fg_color="#009F9F", corner_radius=5).grid(row=0,column=0, sticky='nswe', padx=2, pady=2)
lz1 = ctk.CTkLabel(frame, text='binas', fg_color="#9F009F", corner_radius=5)
lz1.grid(row=0,column=1, sticky='nswe', padx=2, pady=2)

ctk.CTkLabel(frame, text='z2', fg_color="#009F9F", corner_radius=5).grid(row=1,column=0, sticky='nswe', padx=2, pady=2)
lz2 = ctk.CTkLabel(frame, text='pol', fg_color="#9F009F", corner_radius=5)
lz2.grid(row=1,column=1, sticky='nswe', padx=2, pady=2)

def enter(string):
    w = root.focus_get()
    # Check for CTkEntry instead of tk.Entry
    if isinstance(w, ctk.CTkEntry):
        w.insert(ctk.END, string)

def deletee():
    w = root.focus_get()
    # Check for CTkEntry instead of tk.Entry
    if isinstance(w, ctk.CTkEntry):
        w.delete(len(w.get())-1, ctk.END)

def validate(P):
    try:
        float(P)
        return True
    except ValueError:
        return P == "" or P == "-" or P == "+"
vcmd = (frame.register(validate), '%P')

# INPUT HANDLE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Frame para Forma Binómica
_binomicas = ctk.CTkFrame(frame, fg_color="transparent")
_binomicas.columnconfigure((0, 1), weight=1)
entry_bin1_real = ctk.CTkEntry(_binomicas, validate='key', width=100, validatecommand=vcmd)
entry_bin1_real.grid(row=0, column=0, sticky='we', padx=2, pady=2)
entry_bin1_imag = ctk.CTkEntry(_binomicas, validate='key', width=100, validatecommand=vcmd)
entry_bin1_imag.grid(row=0, column=1, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_binomicas, text='i').grid(row=0, column=2)

# Frame para Forma Polar
_polares = ctk.CTkFrame(frame, fg_color="transparent")
_polares.columnconfigure((0, 2), weight=1)
entry_pol1_mod = ctk.CTkEntry(_polares, validate='key', width=100, validatecommand=vcmd)
entry_pol1_mod.grid(row=0, column=0, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_polares, text='cis(').grid(row=0, column=1)
entry_pol1_arg = ctk.CTkEntry(_polares, validate='key', width=100, validatecommand=vcmd)
entry_pol1_arg.grid(row=0, column=2, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_polares, text='°)').grid(row=0, column=3)

# Frame para Forma Exponencial
_exponenciales = ctk.CTkFrame(frame, fg_color="transparent")
_exponenciales.columnconfigure(0, weight=2)
_exponenciales.columnconfigure((2, 4), weight=1)
entry_exp1_mod = ctk.CTkEntry(_exponenciales, validate='key', width=100, validatecommand=vcmd)
entry_exp1_mod.grid(row=0, column=0, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales, text='e^i').grid(row=0, column=1)
entry_exp1_num = ctk.CTkEntry(_exponenciales, validate='key', width=40, validatecommand=vcmd)
entry_exp1_num.grid(row=0, column=2, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales, text='/').grid(row=0, column=3)
entry_exp1_den = ctk.CTkEntry(_exponenciales, validate='key', width=40, validatecommand=vcmd)
entry_exp1_den.grid(row=0, column=4, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales, text='π').grid(row=0, column=5)

# --- WIDGETS PARA EL SEGUNDO NÚMERO (z2) ---
# Frame para Forma Binómica 2
_binomicas1 = ctk.CTkFrame(frame, fg_color="transparent")
_binomicas1.columnconfigure((0, 1), weight=1)
entry_bin2_real = ctk.CTkEntry(_binomicas1, validate='key', width=100, validatecommand=vcmd)
entry_bin2_real.grid(row=0, column=0, sticky='we', padx=2, pady=2)
entry_bin2_imag = ctk.CTkEntry(_binomicas1, validate='key', width=100, validatecommand=vcmd)
entry_bin2_imag.grid(row=0, column=1, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_binomicas1, text='i').grid(row=0, column=2)

# Frame para Forma Polar 2
_polares1 = ctk.CTkFrame(frame, fg_color="transparent")
_polares1.columnconfigure((0, 2), weight=1)
entry_pol2_mod = ctk.CTkEntry(_polares1, validate='key', width=100, validatecommand=vcmd)
entry_pol2_mod.grid(row=0, column=0, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_polares1, text='cis(').grid(row=0, column=1)
entry_pol2_arg = ctk.CTkEntry(_polares1, validate='key', width=100, validatecommand=vcmd)
entry_pol2_arg.grid(row=0, column=2, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_polares1, text='°)').grid(row=0, column=3)

# Frame para Forma Exponencial 2
_exponenciales1 = ctk.CTkFrame(frame, fg_color="transparent")
_exponenciales1.columnconfigure(0, weight=2)
_exponenciales1.columnconfigure((2, 4), weight=1)
entry_exp2_mod = ctk.CTkEntry(_exponenciales1, validate='key', width=100, validatecommand=vcmd)
entry_exp2_mod.grid(row=0, column=0, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales1, text='e^i').grid(row=0, column=1)
entry_exp2_num = ctk.CTkEntry(_exponenciales1, validate='key', width=40, validatecommand=vcmd)
entry_exp2_num.grid(row=0, column=2, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales1, text='/').grid(row=0, column=3)
entry_exp2_den = ctk.CTkEntry(_exponenciales1, validate='key', width=40, validatecommand=vcmd)
entry_exp2_den.grid(row=0, column=4, sticky='we', padx=2, pady=2)
ctk.CTkLabel(_exponenciales1, text='π').grid(row=0, column=5)

ctk.CTkButton(root, text="HALT", command=root.destroy, fg_color="red", hover_color="#C00000").grid(row=8,column=0, pady=10)

###########################################################################
# FRAME 3
###########################################################################
right_frame = ctk.CTkFrame(
    root,
    fg_color="transparent", # Replaces bg, bd, relief
    border_width=2
)
right_frame.grid(row=0, column=6, rowspan=8, sticky='nswe', padx=5, pady=5)
right_frame.columnconfigure(0, weight=1)

# GRÁFICA 1 ==================================================================
ctk.CTkLabel(right_frame, text='Operaciones', fg_color="#550000", anchor='w').grid(row=0,column=0, sticky='we', padx=5, pady=(5,0))
fig1 = Figure(figsize=(3, 2), dpi=96)
ax1 = fig1.add_subplot(111)
ax1.plot([1, 9, 3], [4, 5, 6])
canvas1 = FigureCanvasTkAgg(fig1, master=right_frame)
canvas1.get_tk_widget().grid(row=1,column=0, rowspan=2, sticky='we', padx=5, pady=5)

# GRÁFICA 2 ==================================================================
ctk.CTkLabel(right_frame, text='Resultado', fg_color="#550000", anchor='w').grid(row=3,column=0, sticky='we', padx=5, pady=(5,0))
fig2 = Figure(figsize=(3, 2), dpi=96)
ax2 = fig2.add_subplot(111)
ax2.plot([1, 2, 3], [4, 5, 6])
canvas2 = FigureCanvasTkAgg(fig2, master=right_frame)
canvas2.get_tk_widget().grid(row=4,column=0, rowspan=2, sticky='we', padx=5, pady=5)

# MENU ==================================================================
ctk.CTkButton(root, text='(i)', command=lambda: enter("1"), width=30).grid(row=0,column=7, sticky='wen', padx=2, pady=5)
ctk.CTkButton(root, text='⏾', command=lambda: enter("1"), width=30).grid(row=0,column=8, sticky='wen', padx=2, pady=5)

tipo1 = 0
tipo2 = 0
coperacion = 0

def opera_n(tipo):
    global state
    state = 1
    ntext.grid_forget()
    nspin.grid_forget()
    lresultado.grid_forget()
    ntext.grid(row=0, column=1, sticky='e', padx=2)
    nspin.grid(row=0, column=2, padx=2)
    lresultado.grid(row=0, column=3, columnspan=1, sticky='we', padx=2)
    global coperacion
    match tipo:
        case 1:
            loperacion.configure(text='^')
            ntext.configure(text='elevado a ')
            coperacion = 5
        case 2:
            loperacion.configure(text='√')
            ntext.configure(text='de índice')
            coperacion = 6

potencia = ctk.CTkButton(fbotonescalc, text='x^n', state="disabled", command=lambda: opera_n(1))
potencia.grid(row=4,column=4, padx=2, pady=2)
raiz = ctk.CTkButton(fbotonescalc, text='n√x', state="disabled", command=lambda: opera_n(2))
raiz.grid(row=4,column=5, padx=2, pady=2)

# FRAME OPERACIONES
operation_row_frame = ctk.CTkFrame(frame, fg_color="transparent")
operation_row_frame.grid(row=5, column=0, columnspan=6, sticky='we', pady=5)
operation_row_frame.columnconfigure(3, weight=1)

def opera(tipo):
    global state
    state = 1
    nspin.grid_forget()
    ntext.grid_forget()
    lresultado.grid_forget()
    lresultado.grid(row=0, column=1, columnspan=3, sticky='we', padx=2)
    global coperacion
    match tipo:
        case 1:
            loperacion.configure(text='+')
            coperacion = 1
        case 2:
            loperacion.configure(text='-')
            coperacion = 2
        case 3:
            loperacion.configure(text='*')
            coperacion = 3
        case 4:
            loperacion.configure(text='/')
            coperacion = 4

suma = ctk.CTkButton(fbotonescalc, text='+', state="disabled", command=lambda: opera(1))
suma.grid(row=2,column=4, sticky='we', padx=2, pady=2)
resta = ctk.CTkButton(fbotonescalc, text='-', state="disabled", command=lambda: opera(2))
resta.grid(row=2,column=5, sticky='we', padx=2, pady=2)
multi = ctk.CTkButton(fbotonescalc, text='*', state="disabled", command=lambda: opera(3))
multi.grid(row=3,column=4, sticky='we', padx=2, pady=2)
divi = ctk.CTkButton(fbotonescalc, text='/', state="disabled", command=lambda: opera(4))
divi.grid(row=3,column=5, sticky='we', padx=2, pady=2)

state = 0
stateOP = 0
def corre(tipo, state):
    global stateOP
    if stateOP == 0:
        # States are strings in customtkinter
        suma.configure(state="normal")
        resta.configure(state="normal")
        divi.configure(state="normal")
        multi.configure(state="normal")
        potencia.configure(state="normal")
        raiz.configure(state="normal")
    stateOP = 1
    if state == 0:
        _binomicas.grid_forget()
        _polares.grid_forget()
        _exponenciales.grid_forget()
        global tipo1
        tipo1 = tipo
        match tipo:
            case 1:
                lz1.configure(text="bin")
                _binomicas.grid(row=0, column=2, sticky='nsew')
            case 2:
                lz1.configure(text="pol")
                _polares.grid(row=0, column=2, sticky='nsew')
            case 3:
                lz1.configure(text="exp")
                _exponenciales.grid(row=0, column=2, sticky='nsew')
    else:
        _binomicas1.grid_forget()
        _polares1.grid_forget()
        _exponenciales1.grid_forget()
        global tipo2
        tipo2 = tipo
        match tipo:
            case 1:
                lz2.configure(text="bin")
                _binomicas1.grid(row=1, column=2, sticky='nsew')
            case 2:
                lz2.configure(text="pol")
                _polares1.grid(row=1, column=2, sticky='nsew')
            case 3:
                lz2.configure(text="exp")
                _exponenciales1.grid(row=1, column=2, sticky='nsew')

binomica = ctk.CTkButton(fbotonescalc, text='a+bi', command=lambda: corre(1, state))
binomica.grid(row=0,column=0, columnspan=2, sticky='we', padx=2, pady=2)
polar = ctk.CTkButton(fbotonescalc, text='r cis(°)', command=lambda: corre(2, state))
polar.grid(row=0,column=2, columnspan=2, sticky='we', padx=2, pady=2)
exponencial = ctk.CTkButton(fbotonescalc, text='r e^iθπ', command=lambda: corre(3, state))
exponencial.grid(row=0,column=4, columnspan=2, sticky='we', padx=2, pady=2)

# Using tk.Spinbox as customtkinter does not have a native one. It still works fine.
nspin = tk.Spinbox(operation_row_frame, from_=2, to=20, width=5)
ntext = ctk.CTkLabel(operation_row_frame, text='', fg_color="#ff9f94")
borrar = ctk.CTkButton(fbotonescalc, text='⌫', command=lambda: deletee())
borrar.grid(row=1,column=4, columnspan=2, sticky='we', padx=2, pady=2)

loperacion = ctk.CTkLabel(operation_row_frame, text='+', width=30, fg_color="#07facd", text_color="black")
ntext = ctk.CTkLabel(operation_row_frame, text='', fg_color="#ff9f94")
nspin = tk.Spinbox(operation_row_frame, from_=2, to=20, width=5)
lresultado = ctk.CTkLabel(operation_row_frame, text='=', fg_color="#ff0000", anchor='e')

loperacion.grid(row=0, column=0, sticky='we', padx=2)
lresultado.grid(row=0, column=1, columnspan=3, sticky='we', padx=2)

def computar(tipo1, tipo2, operacion):
    # This entire function's logic remains IDENTICAL.
    v1, v2 = 0.0, 0.0
    try:
        if tipo1 == 1:
            v1 = float(entry_bin1_real.get())
            v2 = float(entry_bin1_imag.get())
        elif tipo1 == 2:
            v1 = float(entry_pol1_mod.get())
            v2 = float(entry_pol1_arg.get())
        elif tipo1 == 3:
            v1 = float(entry_exp1_mod.get())
            v2 = float(entry_exp1_num.get()) / float(entry_exp1_den.get())

        v3, v4 = 0.0, 0.0
        if operacion <= 4:
            if tipo2 == 1:
                v3 = float(entry_bin2_real.get())
                v4 = float(entry_bin2_imag.get())
            elif tipo2 == 2:
                v3 = float(entry_pol2_mod.get())
                v4 = float(entry_pol2_arg.get())
            elif tipo2 == 3:
                v3 = float(entry_exp2_mod.get())
                v4 = float(entry_exp2_num.get()) / float(entry_exp2_den.get())

        resultado = ""
        match operacion:
            case 1:
                resultado = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, 0)
            case 2:
                resultado = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, 1)
            case 3:
                resultado = operations.factor(tipo1, v1, v2, tipo2, v3, v4, 0)
            case 4:
                resultado = operations.factor(tipo1, v1, v2, tipo2, v3, v4, 1)
            case 5:
                n = int(nspin.get())
                resultado = operations.potencia(tipo1, v1, v2, n, 0)
            case 6:
                n = int(nspin.get())
                resultado = operations.potencia(tipo1, v1, v2, n, 1)

        lresultado.configure(text=f"= {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        lresultado.configure(text=f"= Error: {e}")
    except Exception as e:
        lresultado.configure(text=f"= Unexpected Error")


equal = ctk.CTkButton(fbotonescalc, text='=', command=lambda: computar(tipo1,tipo2,coperacion))
equal.grid(row=4, column=1, columnspan=2, sticky='nswe', padx=2, pady=2)

root.mainloop()