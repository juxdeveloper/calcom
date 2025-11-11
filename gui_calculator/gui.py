import tkinter as tk
import conv
from PIL import Image, ImageTk
import operations
import matplotlib.pyplot as plt
import numpy as np 
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
icon_image = tk.PhotoImage(file="logo.png")
root.title('calcom')
root.iconphoto(True, icon_image) 
root.minsize(550, 650)
root.configure(bg='white')
root.option_add("*Font", ("Red Hat Display", 16, "normal"))

# --- CONFIGURACIÓN RESPONSIVE DE LA VENTANA PRINCIPAL ---
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1) # El teclado (fila 2) es la que se expande verticalmente

# --- FRAME SUPERIOR (PANTALLA Z1 y Z2) ---
display_frame = tk.Frame(root, bg="white")
display_frame.grid(row=0, column=0, sticky='nsew')
display_frame.columnconfigure(2, weight=1) # Columna de campos de entrada se expande

# --- FRAME MEDIO (RESULTADOS) ---
operation_row_frame = tk.Frame(root, bg="white")
operation_row_frame.grid(row=1, column=0, sticky='we')
operation_row_frame.columnconfigure(1, weight=1)

# --- FRAME INFERIOR (TECLADO) ---
fbotonescalc = tk.Frame(root, bg="white", relief="flat")
fbotonescalc.grid(row=2, column=0, sticky='nsew')
for i in range(6):
    fbotonescalc.columnconfigure(i, weight=1, uniform="group1")
for i in range(4):
    fbotonescalc.rowconfigure(i, weight=1)

# --- FUNCIONES DE CONTROL DE LA INTERFAZ ---
def enable_operators():
    suma.config(state=tk.NORMAL); resta.config(state=tk.NORMAL)
    multi.config(state=tk.NORMAL); divi.config(state=tk.NORMAL)
    potencia.config(state=tk.NORMAL); raiz.config(state=tk.NORMAL)

def set_z1_format(tipo):
    global tipo1; tipo1 = tipo
    _binomicas.grid_forget(); _polares.grid_forget(); _exponenciales.grid_forget()
    if tipo == 1:
        lz1.config(text="bin"); _binomicas.grid(row=1, column=2, sticky='we')
    elif tipo == 2:
        lz1.config(text="pol"); _polares.grid(row=1, column=2, sticky='we')
    elif tipo == 3:
        lz1.config(text="exp"); _exponenciales.grid(row=1, column=2, sticky='we')
    enable_operators()

def set_z2_format(tipo):
    global tipo2; tipo2 = tipo
    _binomicas1.grid_forget(); _polares1.grid_forget(); _exponenciales1.grid_forget()
    if tipo == 1:
        lz2.config(text="bin"); _binomicas1.grid(row=3, column=2, sticky='we')
    elif tipo == 2:
        lz2.config(text="pol"); _polares1.grid(row=3, column=2, sticky='we')
    elif tipo == 3:
        lz2.config(text="exp"); _exponenciales1.grid(row=3, column=2, sticky='we')

# --- WIDGETS DE LA PANTALLA (display_frame) ---

# SECCIÓN Z1
z1_buttons_frame = tk.Frame(display_frame, bg=display_frame['bg'])
z1_buttons_frame.grid(row=0, column=0, columnspan=3, sticky='we')
for i in range(3): z1_buttons_frame.columnconfigure(i, weight=1)
tk.Button(z1_buttons_frame, text='a+bi', font=("Sitka Display", 12), command=lambda: set_z1_format(1), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=0, sticky='nsew')
tk.Button(z1_buttons_frame, text='r cis(°)', font=("Sitka Display", 12), command=lambda: set_z1_format(2), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=1, sticky='nsew')
tk.Button(z1_buttons_frame, text='r e^iθπ', font=("Sitka Display", 12), command=lambda: set_z1_format(3), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=2, sticky='nsew')

tk.Label(display_frame, text='z1', bg="#009F9F", width=3).grid(row=1, column=0, sticky='nswe')
lz1 = tk.Label(display_frame, text='forma', bg="#FAFEE1", width=9)
lz1.grid(row=1, column=1, sticky='nswe')

# SECCIÓN Z2
z2_buttons_frame = tk.Frame(display_frame, bg=display_frame['bg'])
z2_buttons_frame.grid(row=2, column=0, columnspan=3, sticky='we')
for i in range(3): z2_buttons_frame.columnconfigure(i, weight=1)
tk.Button(z2_buttons_frame, text='a+bi', font=("Sitka Display", 12), command=lambda: set_z2_format(1), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=0, sticky='nsew')
tk.Button(z2_buttons_frame, text='r cis(°)', font=("Sitka Display", 12), command=lambda: set_z2_format(2), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=1, sticky='nsew')
tk.Button(z2_buttons_frame, text='r e^iθπ', font=("Sitka Display", 12), command=lambda: set_z2_format(3), bg="#0A4F6D", fg="white", relief="flat").grid(row=0, column=2, sticky='nsew')

tk.Label(display_frame, text='z2', bg="#009F9F", width=3).grid(row=3, column=0, sticky='nswe')
lz2 = tk.Label(display_frame, text='forma', bg="#FAFEE1", width=9)
lz2.grid(row=3, column=1, sticky='nswe')

# --- WIDGETS DE RESULTADOS (operation_row_frame) ---
loperacion = tk.Label(operation_row_frame, text='op', width=3, bg="#84D0FD")
loperacion.grid(row=0, column=0, rowspan=3, sticky='nswe')
result_container = tk.Frame(operation_row_frame)
result_container.grid(row=0, column=1, rowspan=3, sticky='nswe')
result_container.columnconfigure(0, weight=1)


tk.Label(result_container, text='pol =', anchor='e', bg="#0A4F6D", fg="white", padx=5).grid(row=0, column=0, sticky='we')
#lresultado_bin = tk.Label(result_container, text='bin =', anchor='e', bg="#0A4F6D", fg="white", padx=5)
#lresultado_bin.grid(row=1, column=0, sticky='we')
#lresultado_exp = tk.Label(result_container, text='exp =', anchor='e', bg="#0A4F6D", fg="white", padx=5)
#lresultado_exp.grid(row=2, column=0, sticky='we')


lresultado = tk.Label(result_container, text='pol =', anchor='e', bg="#0A4F6D", fg="white", padx=5)
lresultado.grid(row=1, column=0, sticky='we')
lresultado_bin = tk.Label(result_container, text='bin =', anchor='e', bg="#0A4F6D", fg="white", padx=5)
lresultado_bin.grid(row=1, column=0, sticky='we')
lresultado_exp = tk.Label(result_container, text='exp =', anchor='e', bg="#0A4F6D", fg="white", padx=5)
lresultado_exp.grid(row=2, column=0, sticky='we')

# --- LÓGICA DE ENTRADA Y VALIDACIÓN ---
#ingresar texto
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
vcmd = (root.register(validate), '%P')

# --- FRAMES DE ENTRADA (ahora hijos de display_frame) ---
# INPUT HANDLE
# Frame para Forma Binómica
_binomicas = tk.Frame(display_frame, width=10, relief="solid")
_binomicas.columnconfigure((0, 1), weight=1)
entry_bin1_real = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin1_real.grid(row=0, column=0, sticky='we')
entry_bin1_imag = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin1_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas, text='i', bg="#DBFEEF").grid(row=0, column=2, sticky="ns")

# Frame para Forma Polar
_polares = tk.Frame(display_frame, width=10, relief="solid")
_polares.columnconfigure((0, 2), weight=1)
entry_pol1_mod = tk.Entry(_polares, validate='key', width=8, validatecommand=vcmd, relief="flat",  highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol1_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares, text='cis(', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_pol1_arg = tk.Entry(_polares, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol1_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares, text='°)', bg="#DBFEEF").grid(row=0, column=3, sticky="ns")

# Frame para Forma Exponencial
_exponenciales = tk.Frame(display_frame, width=10, relief="solid")
_exponenciales.columnconfigure(0, weight=2)
_exponenciales.columnconfigure((2, 4), weight=1)
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
_binomicas1 = tk.Frame(display_frame, width=10, relief="solid")
_binomicas1.columnconfigure((0, 1), weight=1)
entry_bin2_real = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin2_real.grid(row=0, column=0, sticky='we')
entry_bin2_imag = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_bin2_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas1, text='i', bg="#DBFEEF").grid(row=0, column=2, sticky='ns')

# Frame para Forma Polar 2
_polares1 = tk.Frame(display_frame, width=10, relief="solid")
_polares1.columnconfigure((0, 2), weight=1)
entry_pol2_mod = tk.Entry(_polares1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares1, text='cis(', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_pol2_arg = tk.Entry(_polares1, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_pol2_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares1, text='°)', bg="#DBFEEF").grid(row=0, column=3, sticky='ns')

# Frame para Forma Exponencial 2
_exponenciales1 = tk.Frame(display_frame, width=10, relief="solid")
_exponenciales1.columnconfigure(0, weight=2)
_exponenciales1.columnconfigure((2, 4), weight=1)
entry_exp2_mod = tk.Entry(_exponenciales1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales1, text='e^i', bg="#DBFEEF").grid(row=0, column=1, sticky='ns')
entry_exp2_num = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_num.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales1, text='/', bg="#DBFEEF").grid(row=0, column=3, sticky='ns')
entry_exp2_den = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground="#DBFEEF")
entry_exp2_den.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales1, text='π', bg="#DBFEEF").grid(row=0, column=5, sticky='ns')

# --- BOTONES DEL TECLADO (fbotonescalc) ---
# Fila 0
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='7', highlightthickness=0, command=lambda: enter("7")).grid(row=0,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='8', highlightthickness=0, command=lambda: enter("8")).grid(row=0,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='9', highlightthickness=0, command=lambda: enter("9")).grid(row=0,column=2, sticky='nswe')
borrar = tk.Button(fbotonescalc, text='⌫', command=lambda: deletee(), bg="#6C100A", fg="white", highlightthickness=0, relief="flat")
borrar.grid(row=0,column=3, columnspan=2, sticky='nswe')
reset = tk.Button(fbotonescalc, text='AC',  relief="flat", highlightthickness=0, bg="#eb971a", fg="black", command=lambda: resetear())
reset.grid(row=0,column=5, rowspan=4, sticky="nswe")

# Fila 1
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='4', highlightthickness=0, command=lambda: enter("4")).grid(row=1,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='5', highlightthickness=0, command=lambda: enter("5")).grid(row=1,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='6', highlightthickness=0, command=lambda: enter("6")).grid(row=1,column=2, sticky='nswe')
suma = tk.Button(fbotonescalc, text='+', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(1))
suma.grid(row=1,column=3, sticky='nswe')
resta = tk.Button(fbotonescalc, text='-', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(2))
resta.grid(row=1,column=4, sticky='nswe')

# Fila 2
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='1', highlightthickness=0, command=lambda: enter("1")).grid(row=2,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='2', highlightthickness=0, command=lambda: enter("2")).grid(row=2,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg="#DBFEEF", text='3', highlightthickness=0, command=lambda: enter("3")).grid(row=2,column=2, sticky='nswe')
multi = tk.Button(fbotonescalc, text='*', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(3))
multi.grid(row=2,column=3, sticky='nswe')
divi = tk.Button(fbotonescalc, text='/', relief="flat", bg="#84D0FD", fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(4))
divi.grid(row=2,column=4, sticky='nswe')

# Fila 3
tk.Button(fbotonescalc,relief="flat", bg="#FAFEE1", text='0', highlightthickness=0, command=lambda: enter("0")).grid(row=3, column=0, sticky='nswe')
equal = tk.Button(fbotonescalc, text='=', command=lambda: computar(tipo1,tipo2,coperacion), bg="#0A4F6D",  highlightthickness=0, fg="white", relief="flat")
equal.grid(row=3, column=1, columnspan=2, sticky='nswe')
potencia = tk.Button(fbotonescalc, text='x^n',  relief="flat", highlightthickness=0, bg="#84D0FD", fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(1))
potencia.grid(row=3,column=3, sticky='nswe')
raiz = tk.Button(fbotonescalc, text='n√x',  relief="flat", highlightthickness=0, bg="#84D0FD", fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(2))
raiz.grid(row=3,column=4, sticky='nswe')

# --- LÓGICA DE CÁLCULO Y FUNCIONES AUXILIARES ---
tipo1 = 0; tipo2 = 0; coperacion = 0

def opera_n(tipo):
    global coperacion
    if tipo == 1:
        loperacion.config(text='^'); coperacion = 5
    elif tipo == 2:
        loperacion.config(text='√'); coperacion = 6

def opera(tipo):
    global coperacion
    if tipo == 1:
        loperacion.config(text='+'); coperacion = 1
    elif tipo == 2:
        loperacion.config(text='-'); coperacion = 2
    elif tipo == 3:
        loperacion.config(text='*'); coperacion = 3
    elif tipo == 4:
        loperacion.config(text='/'); coperacion = 4

# GRAFICAR NÚMERO COMPLEJO
def graficar(grados,r):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot([0, grados], [0, r], color='red', linestyle='-', label='Número Complejo', marker=('*'))
    texto_coordenadas = f'({r:.1f}, {np.degrees(grados):.0f}°)'
    ax.annotate(texto_coordenadas, 
            xy=(grados, r), 
            xytext=(grados, r + 1),
            arrowprops=dict(facecolor='black', shrink=0.03, width=0.4),
            ha='center', va='bottom')
    ax.set_title("Resulado: Número Complejo", va='bottom')
    ax.set_xlabel("Parte Real")
    ax.set_ylabel("Parte Imaginaria")
    ax.yaxis.set_label_coords(-0.1, 0.5)
    ax.legend()
    plt.grid(True)
    plt.show()

# MENU ==================================================================
def info_window():
    creditos = tk.Toplevel(root); creditos.title("Información"); creditos.geometry("300x450")
    img = ImageTk.PhotoImage(Image.open('logo.png').resize((50, 50)))
    logote = tk.Label(creditos, image=img); logote.image = img; logote.pack()
    tk.Label(creditos, text="calcom GUI").pack(pady=10) 
    #tk.Label(new_window, text="fornite").pack()
    tk.Label(creditos, text="juxdeveloper - Joseph").pack()
    tk.Label(creditos, text="juxdeveloper - Joseph").pack()

def computar(tipo1, tipo2, operacion):
    # --- 1. Obtener valores del primer número (z1) ---
    v1, v2 = 0.0, 0.0
    if tipo1 == 1: # Binómica
        v1 = float(entry_bin1_real.get()); v2 = float(entry_bin1_imag.get())
    elif tipo1 == 2: # Polar
        v1 = float(entry_pol1_mod.get()); v2 = float(entry_pol1_arg.get())
    elif tipo1 == 3: # Exponencial
        v1 = float(entry_exp1_mod.get()); v2 = float(entry_exp1_num.get()) / float(entry_exp1_den.get())

    # --- 2. Obtener valores del segundo número (z2), si es necesario ---
    v3, v4 = 0.0, 0.0
    if operacion <= 4:
        if tipo2 == 1: # Binómica
            v3 = float(entry_bin2_real.get()); v4 = float(entry_bin2_imag.get())
        elif tipo2 == 2: # Polar
            v3 = float(entry_pol2_mod.get()); v4 = float(entry_pol2_arg.get())
        elif tipo2 == 3: # Exponencial
            v3 = float(entry_exp2_mod.get()); v4 = float(entry_exp2_num.get()) / float(entry_exp2_den.get())
    
    # --- 3. Realizar el cálculo y las conversiones ---
    res_bin = (0, 0); res_pol = (0, 0); res_exp = (0, (0, 1))
    n = 2 # Placeholder para nspin

    if operacion in [1, 2]: # Suma y Resta devuelven binómica
        raw_result = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, operacion - 1)
        res_bin = raw_result
        res_pol = conv.bin_pol(res_bin[0], res_bin[1])
        # Asumimos que conv.bin_exp existe y devuelve una tupla (módulo, (numerador, denominador))
        # res_exp = conv.bin_exp(res_bin[0], res_bin[1]) 
    
    elif operacion in [3, 4, 5, 6]: # El resto devuelve polar
        if operacion <= 4: # Multiplicación y División
            raw_result = operations.factor(tipo1, v1, v2, tipo2, v3, v4, operacion - 3)
        else: # Potencia y Raíz
            raw_result = operations.potencia(tipo1, v1, v2, n, operacion - 5)
        
        res_pol = raw_result
        res_bin = conv.pol_bin(res_pol[0], res_pol[1])
        # Asumimos que conv.pol_exp existe y devuelve una tupla (módulo, (numerador, denominador))
        # res_exp = conv.pol_exp(res_pol[0], res_pol[1])

    # --- 4. Mostrar el resultado ---
    pol_str = f"pol = {res_pol[0]:.4f} cis({res_pol[1]:.4f}°)"
    bin_str = f"bin = {res_bin}" # Imprime la tupla directamente como pediste
    exp_str = f"exp = {res_exp}" # Imprime la tupla directamente como pediste

    lresultado.config(text=pol_str)
    lresultado_bin.config(text=bin_str)
    lresultado_exp.config(text=exp_str)
    
    # --- 5. Graficar ---
    # La función graficar espera radianes, pero tus resultados están en grados
    arg_rad = np.radians(res_pol[1])
    graficar(arg_rad, res_pol[0])

def resetear():
    """
    Reinicia la calculadora a su estado inicial.
    Limpia todos los campos, oculta widgets, y resetea variables de estado.
    """
    # Declarar las variables globales que vamos a modificar
    global tipo1, tipo2, coperacion
    
    # 1. Reiniciar las variables de estado a sus valores iniciales
    tipo1 = 0; tipo2 = 0; coperacion = 0
    
    # 2. Limpiar todos los campos de entrada (Entry)
    entry_bin1_real.delete(0, tk.END); entry_bin1_imag.delete(0, tk.END)
    entry_pol1_mod.delete(0, tk.END); entry_pol1_arg.delete(0, tk.END)
    entry_exp1_mod.delete(0, tk.END); entry_exp1_num.delete(0, tk.END); entry_exp1_den.delete(0, tk.END)
    entry_bin2_real.delete(0, tk.END); entry_bin2_imag.delete(0, tk.END)
    entry_pol2_mod.delete(0, tk.END); entry_pol2_arg.delete(0, tk.END)
    entry_exp2_mod.delete(0, tk.END); entry_exp2_num.delete(0, tk.END); entry_exp2_den.delete(0, tk.END)
    
    # 3. Ocultar todos los frames de entrada de números
    _binomicas.grid_forget(); _polares.grid_forget(); _exponenciales.grid_forget()
    _binomicas1.grid_forget(); _polares1.grid_forget(); _exponenciales1.grid_forget()

    # 4. Restablecer el texto de las etiquetas a su estado original
    lz1.config(text='forma'); lz2.config(text='forma')
    loperacion.config(text='op'); lresultado.config(text='pol =')
    lresultado_bin.config(text='bin ='); lresultado_exp.config(text='exp =')
    
    # 5. Deshabilitar los botones de operaciones
    suma.config(state=tk.DISABLED); resta.config(state=tk.DISABLED)
    multi.config(state=tk.DISABLED); divi.config(state=tk.DISABLED)
    potencia.config(state=tk.DISABLED); raiz.config(state=tk.DISABLED)

root.mainloop()