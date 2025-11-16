import tkinter as tk                        # Para GUI
import conv                                 # Módulo propio para conversiones
import operations                           # Módulo propio para operaciones
import matplotlib.pyplot as plt             # Para graficar
#import numpy as np                             # Procesar para graficar
# importado donde se ocupe para optimizar
from PIL import Image, ImageTk              # Para mostrar imágenes
from fractions import Fraction              # Para procesar fracciones de forma exponencial

# Colores del tema, como variables para poder ser personalizado
# fácilmente
C_BORRAR = '#313d5a'
C_IGUAL = '#525072'
C_RESULTADOS = "#2f6373"
C_PANTALLA = "#2f6373"
C_OPERACIONES = "#B5ADD2"
C_INFO_OPERACIONES = "#9f94ba"
C_CLARO = "#DBD8EA"
C_NUMEROS = "#CBC5EA"
C_AC="#73628A"
C_FLECHITAS = "#DAFF7D"
C_ERROR="#FFA38B"

#### GENERATED FOR PYINSTALLER ####
import sys
import os
#### GENERATED FOR PYINSTALLER ####

###########################################
# Lógica inicial de GUI planteada y más o menos respetada
###########################################
# 1. BOTÓN Pon el primer tipo de número
#       Muestra tipo
#       Muestra form
#       Maneja entrada
#       Actualiza gráfico
# 2. Tecla ENTER
#       Valida entrada
# 3. Selecciona operador
# 4. BOTÓN Pon el 2do tipo de número
#       Muestra tipo
#       Muestra form
#       Maneja entrada
#       Actualiza gráfico
# 5. Tecla ENTER
#       Valida entrada

#### GENERATED FOR PYINSTALLER ####
def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)
#### GENERATED FOR PYINSTALLER ####


# Configura la ventana principal
root = tk.Tk()
#### GENERATED FOR PYINSTALLER ####
icon_image = tk.PhotoImage(file=resource_path("logo.png"))
#### GENERATED FOR PYINSTALLER ####
root.title('calcom')
root.iconphoto(True, icon_image) 
root.minsize(550, 450)
root.configure(bg='white')
# Fuente default
root.option_add("*Font", ("Microsoft Sans Serif", 16, "normal"))

# --- CONFIGURACIÓN RESPONSIVE DE LA VENTANA PRINCIPAL ---
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1) # El teclado (fila 2) es la que se expande verticalmente

# --- FRAME SUPERIOR (PANTALLA Z1 y Z2) ---
display_frame = tk.Frame(root, bg=C_CLARO)
display_frame.grid(row=0, column=0, sticky='nsew')
display_frame.columnconfigure(2, weight=1) # Columna de campos de entrada se expande

# --- FRAME MEDIO (RESULTADOS) ---
operation_row_frame = tk.Frame(root)
operation_row_frame.grid(row=1, column=0, sticky='we')
operation_row_frame.columnconfigure(1, weight=1)

# --- FRAME INFERIOR (TECLADO) ---
fbotonescalc = tk.Frame(root, bg="white", relief="flat")
fbotonescalc.grid(row=2, column=0, sticky='nsew')
for i in range(6):
	fbotonescalc.columnconfigure(i, weight=1, uniform="group1")
for i in range(4):
	fbotonescalc.rowconfigure(i, weight=1)

# En todos los frames se normaliza el tamaño
# y se busca un diseño responsive, que se adapte a la ventana

# --- FUNCIONES DE CONTROL DE LA INTERFAZ ---
# Habilita botones
def enable_operators():
	suma.config(state=tk.NORMAL); resta.config(state=tk.NORMAL)
	multi.config(state=tk.NORMAL); divi.config(state=tk.NORMAL)
	potencia.config(state=tk.NORMAL); raiz.config(state=tk.NORMAL)
	conjugado.config(state=tk.NORMAL)

# Establece el tipo de z1
def set_z1_format(tipo):
	global tipo1; tipo1 = tipo
	# Quita de pantalla cosas innecesarias
	_binomicas.grid_forget(); _polares.grid_forget(); _exponenciales.grid_forget()
	if tipo == 1:
		lz1.config(text="bin"); _binomicas.grid(row=1, column=2, sticky='we')
	elif tipo == 2:
		lz1.config(text="pol"); _polares.grid(row=1, column=2, sticky='we')
	elif tipo == 3:
		lz1.config(text="exp"); _exponenciales.grid(row=1, column=2, sticky='we')
	enable_operators()

# Establece el tipo de z2
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

# Feame que contiene botones de tipo de z
z1_buttons_frame = tk.Frame(display_frame, bg=display_frame['bg'])
z1_buttons_frame.grid(row=0, column=0, columnspan=3, sticky='we')
for i in range(3): z1_buttons_frame.columnconfigure(i, weight=1)
tk.Button(z1_buttons_frame, text='a+bi', font=("Times New Roman", 14), command=lambda: set_z1_format(1), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=0, sticky='nsew')
tk.Button(z1_buttons_frame, text='r cis(°)', font=("Times New Roman", 14), command=lambda: set_z1_format(2), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=1, sticky='nsew')
tk.Button(z1_buttons_frame, text='r e^iθπ', font=("Times New Roman", 14), command=lambda: set_z1_format(3), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=2, sticky='nsew')

tk.Label(display_frame, text='z1', bg=C_INFO_OPERACIONES, width=3).grid(row=1, column=0, sticky='nswe')
lz1 = tk.Label(display_frame, text='forma', bg=C_CLARO, width=9)
lz1.grid(row=1, column=1, sticky='nswe')

# SECCIÓN Z2
z2_buttons_frame = tk.Frame(display_frame, bg=display_frame['bg'])
z2_buttons_frame.grid(row=2, column=0, columnspan=3, sticky='we')
for i in range(3): z2_buttons_frame.columnconfigure(i, weight=1)
tk.Button(z2_buttons_frame, text='a+bi', font=("Times New Roman", 14), command=lambda: set_z2_format(1), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=0, sticky='nsew')
tk.Button(z2_buttons_frame, text='r cis(°)', font=("Times New Roman", 14), command=lambda: set_z2_format(2), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=1, sticky='nsew')
tk.Button(z2_buttons_frame, text='r e^iθπ', font=("Times New Roman", 14), command=lambda: set_z2_format(3), bg=C_IGUAL, fg="white", relief="flat").grid(row=0, column=2, sticky='nsew')

z2_static_label = tk.Label(display_frame, text='z2', bg=C_INFO_OPERACIONES, width=3)
z2_static_label.grid(row=3, column=0, sticky='nswe')
lz2 = tk.Label(display_frame, text='forma', bg=C_CLARO, width=9)
lz2.grid(row=3, column=1, sticky='nswe')



# --- WIDGETS DE RESULTADOS (operation_row_frame) ---
loperacion = tk.Label(operation_row_frame, text='op', width=3, bg=C_OPERACIONES)
loperacion.grid(row=0, column=0, rowspan=5, sticky='nswe')
result_container = tk.Frame(operation_row_frame, bg=C_IGUAL)
result_container.grid(row=0, column=1, rowspan=5, sticky='nswe')
result_container.columnconfigure(1, weight=1)

# Texto estático a la izquierda
l_static_pol = tk.Label(result_container, text='pol =', anchor='w', bg=C_IGUAL, fg="white", padx=5)
l_static_bin = tk.Label(result_container, text='bin =', anchor='w', bg=C_IGUAL, fg="white", padx=5)
l_static_exp = tk.Label(result_container, text='exp =', anchor='w', bg=C_IGUAL, fg="white", padx=5)


# Selector para n de raíz o potencia
n_text_label = tk.Label(result_container, text='', anchor='w', bg=C_IGUAL, fg="white", padx=5)
n_spinbox = tk.Spinbox(result_container, from_=2, to=20, width=3)

# Texto dinámico con resultados
lresultado_pol = tk.Label(result_container, text='', font=("Times New Roman", 16), anchor='e', bg=C_IGUAL, fg="white")
lresultado_bin = tk.Label(result_container, text='', font=("Times New Roman", 16), anchor='e', bg=C_IGUAL, fg="white")
lresultado_exp = tk.Label(result_container, text='', font=("Times New Roman", 16), anchor='e', bg=C_IGUAL, fg="white")

# Palomitas de adorno, para hacer más creíble el resultado
lcheck_pol = tk.Label(result_container, text='', fg=C_FLECHITAS, anchor='e', bg=C_IGUAL, padx=5)
lcheck_bin = tk.Label(result_container, text='', fg=C_FLECHITAS, anchor='e', bg=C_IGUAL, padx=5)
lcheck_exp = tk.Label(result_container, text='', fg=C_FLECHITAS, anchor='e', bg=C_IGUAL, padx=5)


# En el caso de la raíz, darle su propio formato
roots_results_frame = tk.Frame(result_container, bg=C_IGUAL)
roots_results_frame.columnconfigure((0,1), weight=1)
root_result_labels = []
for i in range(10): 
	label = tk.Label(roots_results_frame, text='', anchor='center', bg=C_IGUAL, fg="white")
	label.grid(row=i//2, column=i%2, sticky='we')
	root_result_labels.append(label)


# --- LÓGICA DE ENTRADA Y VALIDACIÓN ---

# ingresar texto con botón
def enter(string):
	w = root.focus_get()
	if isinstance(w, tk.Entry):
		w.insert(tk.END, string)

# borrar con botón
def deletee():
	w = root.focus_get()
	if isinstance(w, tk.Entry):
		w.delete(len(w.get())-1, tk.END)

# restringir entrada a solo números decimales con +/-
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
entry_bin1_real = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_bin1_real.grid(row=0, column=0, sticky='we')
entry_bin1_imag = tk.Entry(_binomicas, validate='key', width=8, validatecommand=vcmd,relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_bin1_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas, text='i', bg=C_NUMEROS).grid(row=0, column=2, sticky="ns")

# Frame para Forma Polar
_polares = tk.Frame(display_frame, width=10, relief="solid")
_polares.columnconfigure((0, 2), weight=1)
entry_pol1_mod = tk.Entry(_polares, validate='key', width=8, validatecommand=vcmd, relief="flat",  highlightthickness=3, highlightbackground=C_NUMEROS)
entry_pol1_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares, text='cis(', bg=C_NUMEROS).grid(row=0, column=1, sticky='ns')
entry_pol1_arg = tk.Entry(_polares, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_pol1_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares, text='°)', bg=C_NUMEROS).grid(row=0, column=3, sticky="ns")

# Frame para Forma Exponencial
_exponenciales = tk.Frame(display_frame, width=10, relief="solid")
_exponenciales.columnconfigure(0, weight=2)
_exponenciales.columnconfigure((2, 4), weight=1)
entry_exp1_mod = tk.Entry(_exponenciales, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp1_mod.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales, text='e^i', bg=C_NUMEROS).grid(row=0, column=1, sticky='ns')
entry_exp1_num = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp1_num.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales, text='/', bg=C_NUMEROS).grid(row=0, column=3, sticky='ns')
entry_exp1_den = tk.Entry(_exponenciales, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp1_den.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales, text='π', bg=C_NUMEROS).grid(row=0, column=5, sticky='ns')

# --- WIDGETS PARA EL SEGUNDO NÚMERO (z2) ---
# Frame para Forma Binómica 2
_binomicas1 = tk.Frame(display_frame, width=10, relief="solid")
_binomicas1.columnconfigure((0, 1), weight=1)
entry_bin2_real = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_bin2_real.grid(row=0, column=0, sticky='we')
entry_bin2_imag = tk.Entry(_binomicas1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_bin2_imag.grid(row=0, column=1, sticky='we')
tk.Label(_binomicas1, text='i', bg=C_NUMEROS).grid(row=0, column=2, sticky='ns')

# Frame para Forma Polar 2
_polares1 = tk.Frame(display_frame, width=10, relief="solid")
_polares1.columnconfigure((0, 2), weight=1)
entry_pol2_mod = tk.Entry(_polares1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_pol2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_polares1, text='cis(', bg=C_NUMEROS).grid(row=0, column=1, sticky='ns')
entry_pol2_arg = tk.Entry(_polares1, validate='key', width=8,validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_pol2_arg.grid(row=0, column=2, sticky='we')
tk.Label(_polares1, text='°)', bg=C_NUMEROS).grid(row=0, column=3, sticky='ns')

# Frame para Forma Exponencial 2
_exponenciales1 = tk.Frame(display_frame, width=10, relief="solid")
_exponenciales1.columnconfigure(0, weight=2)
_exponenciales1.columnconfigure((2, 4), weight=1)
entry_exp2_mod = tk.Entry(_exponenciales1, validate='key', width=8, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp2_mod.grid(row=0, column=0, sticky='we')
tk.Label(_exponenciales1, text='e^i', bg=C_NUMEROS).grid(row=0, column=1, sticky='ns')
entry_exp2_num = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp2_num.grid(row=0, column=2, sticky='we')
tk.Label(_exponenciales1, text='/', bg=C_NUMEROS).grid(row=0, column=3, sticky='ns')
entry_exp2_den = tk.Entry(_exponenciales1, validate='key', width=3, validatecommand=vcmd, relief="flat", highlightthickness=3, highlightbackground=C_NUMEROS)
entry_exp2_den.grid(row=0, column=4, sticky='we')
tk.Label(_exponenciales1, text='π', bg=C_NUMEROS).grid(row=0, column=5, sticky='ns')


# --- BOTONES DEL TECLADO (fbotonescalc) ---
# Fila 0
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='7', highlightthickness=0, command=lambda: enter("7")).grid(row=0,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='8', highlightthickness=0, command=lambda: enter("8")).grid(row=0,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='9', highlightthickness=0, command=lambda: enter("9")).grid(row=0,column=2, sticky='nswe')
conjugado = tk.Button(fbotonescalc, text='z̅',  relief="flat", highlightthickness=0, bg=C_OPERACIONES, fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_unitaria(7))
conjugado.grid(row=0,column=3, sticky='nswe')
borrar = tk.Button(fbotonescalc, text='⌫', command=lambda: deletee(), bg=C_BORRAR, fg="white", highlightthickness=0, relief="flat")
borrar.grid(row=0,column=4, sticky='nswe')
reset = tk.Button(fbotonescalc, text='AC',  relief="flat", highlightthickness=0, bg=C_AC, fg="white", command=lambda: resetear())
reset.grid(row=0,column=5, rowspan=4, sticky="nswe")

# Fila 1
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='4', highlightthickness=0, command=lambda: enter("4")).grid(row=1,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='5', highlightthickness=0, command=lambda: enter("5")).grid(row=1,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='6', highlightthickness=0, command=lambda: enter("6")).grid(row=1,column=2, sticky='nswe')
suma = tk.Button(fbotonescalc, text='+', relief="flat", bg=C_OPERACIONES, fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(1))
suma.grid(row=1,column=3, sticky='nswe')
resta = tk.Button(fbotonescalc, text='-', relief="flat", bg=C_OPERACIONES, fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(2))
resta.grid(row=1,column=4, sticky='nswe')

# Fila 2
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='1', highlightthickness=0, command=lambda: enter("1")).grid(row=2,column=0, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='2', highlightthickness=0, command=lambda: enter("2")).grid(row=2,column=1, sticky='nswe')
tk.Button(fbotonescalc,relief="flat", bg=C_NUMEROS, text='3', highlightthickness=0, command=lambda: enter("3")).grid(row=2,column=2, sticky='nswe')
multi = tk.Button(fbotonescalc, text='*', relief="flat", bg=C_OPERACIONES, fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(3))
multi.grid(row=2,column=3, sticky='nswe')
divi = tk.Button(fbotonescalc, text='/', relief="flat", bg=C_OPERACIONES, fg="black", highlightthickness=0, disabledforeground="gray", state=tk.DISABLED, command=lambda: opera(4))
divi.grid(row=2,column=4, sticky='nswe')

# Fila 3
tk.Button(fbotonescalc,relief="flat", bg=C_CLARO, text='0', highlightthickness=0, command=lambda: enter("0")).grid(row=3, column=0, sticky='nswe')
equal = tk.Button(fbotonescalc, text='=', command=lambda: computar(tipo1,tipo2,coperacion), bg=C_IGUAL,  highlightthickness=0, fg="white", relief="flat")
equal.grid(row=3, column=1, columnspan=2, sticky='nswe')
potencia = tk.Button(fbotonescalc, text='x^n',  relief="flat", highlightthickness=0, bg=C_OPERACIONES, fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(1))
potencia.grid(row=3,column=3, sticky='nswe')
raiz = tk.Button(fbotonescalc, text='n√x',  relief="flat", highlightthickness=0, bg=C_OPERACIONES, fg="black", disabledforeground="gray", state=tk.DISABLED, command=lambda: opera_n(2))
raiz.grid(row=3,column=4, sticky='nswe')





# --- LÓGICA DE CÁLCULO Y FUNCIONES AUXILIARES ---
tipo1 = 0; tipo2 = 0; coperacion = 0

# Ocultar z2 para operaciones unitarias como conjugado, potencia y raíz
def hide_z2():
	z2_buttons_frame.grid_forget()
	z2_static_label.grid_forget()
	lz2.grid_forget()
	_binomicas1.grid_forget(); _polares1.grid_forget(); _exponenciales1.grid_forget()

# Volver a mostrar
def show_z2():
	z2_buttons_frame.grid(row=2, column=0, columnspan=3, sticky='we')
	z2_static_label.grid(row=3, column=0, sticky='nswe')
	lz2.grid(row=3, column=1, sticky='nswe')

# Mostrar resultado de operaciones
def show_standard_results_ui():
	n_text_label.grid_remove(); n_spinbox.grid_remove()
	roots_results_frame.grid_remove()
	l_static_pol.grid(row=0, column=0, sticky='w'); l_static_bin.grid(row=1, column=0, sticky='w'); l_static_exp.grid(row=2, column=0, sticky='w')
	lresultado_pol.grid(row=0, column=1, sticky='we'); lresultado_bin.grid(row=1, column=1, sticky='we'); lresultado_exp.grid(row=2, column=1, sticky='we')
	lcheck_pol.grid(row=0, column=2, sticky='e'); lcheck_bin.grid(row=1, column=2, sticky='e'); lcheck_exp.grid(row=2, column=2, sticky='e')

# Para el caso de la raíz
def show_power_root_ui():
	l_static_pol.grid_remove(); l_static_bin.grid_remove(); l_static_exp.grid_remove()
	lresultado_pol.grid_remove(); lresultado_bin.grid_remove(); lresultado_exp.grid_remove()
	lcheck_pol.grid_remove(); lcheck_bin.grid_remove(); lcheck_exp.grid_remove()
	n_text_label.grid(row=0, column=0, sticky='e'); n_spinbox.grid(row=0, column=1, sticky='w')

# Operanción unitaria
def opera_unitaria(tipo):
	global coperacion
	show_standard_results_ui()
	hide_z2()
	if tipo == 7:
		loperacion.config(text='z̅'); coperacion = 7

# operando raíz/potencia
def opera_n(tipo):
	global coperacion
	show_power_root_ui()
	hide_z2()
	if tipo == 1:
		loperacion.config(text='^'); coperacion = 5; n_text_label.config(text='elevado a:')
	elif tipo == 2:
		loperacion.config(text='√'); coperacion = 6; n_text_label.config(text='de índice:')

# operando
def opera(tipo):
	global coperacion
	show_standard_results_ui()
	show_z2()
	if tipo == 1:
		loperacion.config(text='+'); coperacion = 1
	elif tipo == 2:
		loperacion.config(text='-'); coperacion = 2
	elif tipo == 3:
		loperacion.config(text='*'); coperacion = 3
	elif tipo == 4:
		loperacion.config(text='/'); coperacion = 4

# Parsear número para que se vea bien
def format_number(num):
	return f'{num:.4f}'.rstrip('0').rstrip('.')

# GRAFICAR NÚMERO COMPLEJO
def graficar(resultados_polares):
	import numpy as np
	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot(111, polar=True)
	
	# Para cada resultado polar, ir graficándolo
	for i, (radianes, r) in enumerate(resultados_polares):
		label = 'Resultado' if len(resultados_polares) == 1 else f'Raíz {i+1}'
		ax.plot([0, radianes], [0, r], label=label, marker='*')
		
		grados_para_mostrar = np.degrees(radianes)
		texto_coordenadas = f'({format_number(r)}, {format_number(grados_para_mostrar)}°)'
		
		ax.annotate(texto_coordenadas, 
				xy=(radianes, r), 
				xytext=(radianes, r + 1),
				arrowprops=dict(facecolor='black', shrink=0.03, width=0.4),
				ha='center', va='bottom')

	ax.set_title("Resultado(s) en el Plano Complejo", va='bottom', fontsize=14)
	ax.legend()
	plt.grid(True)
	plt.show()

# MENU ==================================================================
# Los çréditos no podían faltar, aunque el recolector de basura se llevaba 
# las imágenes jajaja
def info_window():
	creditos = tk.Toplevel(root); creditos.title("Información"); #creditos.geometry("300x450")
	creditos.configure(bg=C_NUMEROS)
	creditos.columnconfigure(0,weight=1)
	creditos.option_add("*Font", ("Microsoft Sans Serif", 14, "normal"))
	creditos.resizable(False, False) 

	#### GENERATED FOR PYINSTALLER ####
	img = ImageTk.PhotoImage(Image.open(resource_path('logo.png')).resize((50, 50)))
	#### GENERATED FOR PYINSTALLER ####
	logote = tk.Label(creditos, image=img); logote.image = img; logote.grid(row=0, column=0)
	tk.Label(creditos, text="calcom GUI 2.0", bg=C_OPERACIONES, font=("Microsoft Sans Serif", 18, "bold")).grid(row=1, column=0)
	#tk.Label(new_window, text="fornite").pack()

	tk.Label(creditos, text="Lead developer & Design", font=("Microsoft Sans Serif", 14, "bold")).grid(row=2, column=0)
	tk.Label(creditos, text="juxdeveloper - Joseph").grid(row=3, column=0)
	#### GENERATED FOR PYINSTALLER ####
	img = ImageTk.PhotoImage(Image.open(resource_path('joseph.jpg')).resize((50, 50)))
	#### GENERATED FOR PYINSTALLER ####
	pp = tk.Label(creditos, image=img); pp.image = img; pp.grid(row=4, column=0)

	tk.Label(creditos, text="Ideas, HR & matplotlib").grid(row=5, column=0)
	tk.Label(creditos, text="thxp2 - Hanniel").grid(row=6, column=0)
	#### GENERATED FOR PYINSTALLER ####
	img = ImageTk.PhotoImage(Image.open(resource_path('hanniel.jpg')).resize((50, 50)))
	#### GENERATED FOR PYINSTALLER ####
	pp = tk.Label(creditos, image=img); pp.image = img; pp.grid(row=7, column=0)

	tk.Label(creditos, text="Innovation").grid(row=8, column=0)
	tk.Label(creditos, text="adalidgonzalez57 - Adalid").grid(row=9, column=0)
	#### GENERATED FOR PYINSTALLER ####
	img = ImageTk.PhotoImage(Image.open(resource_path('adalid.jpeg')).resize((50, 50)))
	#### GENERATED FOR PYINSTALLER ####
	pp = tk.Label(creditos, image=img); pp.image = img; pp.grid(row=10, column=0)

	tk.Label(creditos, text="Early tests").grid(row=11, column=0)
	tk.Label(creditos, text="karoljaredsosa-hub - Jared").grid(row=12, column=0)
	#### GENERATED FOR PYINSTALLER ####
	img = ImageTk.PhotoImage(Image.open(resource_path('jared.png')).resize((50, 50)))
	#### GENERATED FOR PYINSTALLER ####
	pp = tk.Label(creditos, image=img); pp.image = img; pp.grid(row=13, column=0)

info = tk.Button(root, text='🛈 info',  relief="flat", highlightthickness=0, bg=C_INFO_OPERACIONES, fg="black", command=info_window)
info.grid(row=3,column=0, sticky='nswe')


# Función maestra al calcular
def computar(tipo1, tipo2, operacion):
	import numpy as np
	try:
		# --- 1. Obtener valores del primer número (z1) ---
		v1, v2 = 0.0, 0.0
		if tipo1 == 1: # Binómica
			v1 = float(entry_bin1_real.get()); v2 = float(entry_bin1_imag.get())
		elif tipo1 == 2: # Polar
			v1 = float(entry_pol1_mod.get()); v2 = float(entry_pol1_arg.get())
		elif tipo1 == 3: # Exponencial
			num = float(entry_exp1_num.get()); den = float(entry_exp1_den.get())
			v1 = float(entry_exp1_mod.get()); v2 = num / den

		# --- 2. Obtener valores del segundo número (z2), si es necesario ---
		v3, v4 = 0.0, 0.0
		if operacion <= 4:
			if tipo2 == 1: # Binómica
				v3 = float(entry_bin2_real.get()); v4 = float(entry_bin2_imag.get())
			elif tipo2 == 2: # Polar
				v3 = float(entry_pol2_mod.get()); v4 = float(entry_pol2_arg.get())
			elif tipo2 == 3: # Exponencial
				num = float(entry_exp2_num.get()); den = float(entry_exp2_den.get())
				v3 = float(entry_exp2_mod.get()); v4 = num / den
		
		# --- 3. Realizar el cálculo ---

		# Para suma y resta, mult y div (ids del 1 al 4 según a operations.py)
		if operacion in [1, 2, 3, 4]: 
			show_standard_results_ui()

			# Crear variables para guardar los resultados
			res_bin = (0, 0)
			res_pol = (0, 0)
			

			# Si es suma/resta se usa función adición de operations.py
			if operacion <= 2: 
				res_bin = operations.adicion(tipo1, v1, v2, tipo2, v3, v4, operacion - 1)
				res_pol = conv.bin_pol(res_bin[0], res_bin[1])
			else:
			# Si no, pues factor()
				res_pol = operations.factor(tipo1, v1, v2, tipo2, v3, v4, operacion - 3)
				res_bin = conv.pol_bin(res_pol[0], res_pol[1])


			# Fortaeo y parseo los cálculos para que se vean bien en el label
			# Cambio el texto del label, lo que lo hace dinámico

			# Polar
			r_pol_str = format_number(res_pol[0]); g_pol_str = format_number(res_pol[1])
			lresultado_pol.config(text=f"{r_pol_str} cis({g_pol_str}°)")

			# Binómica
			a_bin_str = format_number(res_bin[0]); b_bin_val = res_bin[1]
			signo = "+" if b_bin_val >= 0 else "-"; b_bin_str_abs = format_number(abs(b_bin_val))
			lresultado_bin.config(text=f"{a_bin_str} {signo} {b_bin_str_abs}i")

			# Exponencial
			res_exp_tuple = conv.pol_exp(res_pol[0], res_pol[1])
			r_exp_str = format_number(res_exp_tuple[0]); frac = Fraction(res_exp_tuple[1]).limit_denominator()
			theta_str = f"{frac.numerator}" if frac.denominator == 1 else f"{frac.numerator}/{frac.denominator}"
			lresultado_exp.config(text=f"{r_exp_str} e^i {theta_str}π")


			# Mostrar las flechitas verdes
			lcheck_pol.config(text='✔'); lcheck_bin.config(text='✔'); lcheck_exp.config(text='✔')

			# Guardar en lista el conjunto de resultados
			# para graficar
			resultados_para_graficar = [(np.radians(res_pol[1]), res_pol[0])]

			# Pasa los resultados y realiza lo necesario para graficar
			graficar(resultados_para_graficar)





			# Ahora si no es suma, resta, mult y div
			# id 5-6, o sea potencia y raiz
		elif operacion in [5, 6]: 

			# Mostramos un spinbox y guardamos su valor
			# el cual es el índice o exponente de raíz/potencia respectivamente
			n = int(n_spinbox.get())
			soluciones = operations.potencia(tipo1, v1, v2, n, operacion - 5)
			
			# Si es potencia
			if operacion == 5: 
				show_power_root_ui()
				lresultado_pol.grid(row=1, column=0, columnspan=3, sticky='we')
				# Solo muestra cis, lo más conveniente
				r_str = format_number(soluciones[0]); g_str = format_number(soluciones[1])
				lresultado_pol.config(text=f"{r_str} cis({g_str}°)")
				
				resultados_para_graficar = [(np.radians(soluciones[1]), soluciones[0])]
				graficar(resultados_para_graficar)
			else: 
			# Si es raíz
				show_power_root_ui()
				roots_results_frame.grid(row=0, column=0, columnspan=3, rowspan=5, sticky='nsew')
				for label in root_result_labels: label.config(text="") 
			   
			# Va iterando en la cantidad de soluciones y mostrando en pantalla
				for i, sol in enumerate(soluciones):
					if i < len(root_result_labels):
						r_str = format_number(sol[0]); g_str = format_number(sol[1])
						root_result_labels[i].config(text=f"z{i+1}= {r_str} cis({g_str}°)")
				
				resultados_para_graficar = [(np.radians(g), r) for r, g in soluciones]
				graficar(resultados_para_graficar)
		
		elif operacion == 7: # Operación Conjugado
			show_standard_results_ui()

			# Llama a la operación del conjugado
			res_bin = operations.conjugado(tipo1,v1,v2)
			res_pol = conv.bin_pol(res_bin[0], res_bin[1])

			# Parsea formato y muestra pol
			r_pol_str = format_number(res_pol[0]); g_pol_str = format_number(res_pol[1])
			lresultado_pol.config(text=f"{r_pol_str} cis({g_pol_str}°)")

			# Parsea formato y muestra bin
			a_bin_str = format_number(res_bin[0]); b_bin_val = res_bin[1]
			signo = "+" if b_bin_val >= 0 else "-"; b_bin_str_abs = format_number(abs(b_bin_val))
			lresultado_bin.config(text=f"{a_bin_str} {signo} {b_bin_str_abs}i")

			# Parsea formato y muestra exp
			res_exp_tuple = conv.pol_exp(res_pol[0], res_pol[1])
			r_exp_str = format_number(res_exp_tuple[0]); frac = Fraction(res_exp_tuple[1]).limit_denominator()
			theta_str = f"{frac.numerator}" if frac.denominator == 1 else f"{frac.numerator}/{frac.denominator}"
			lresultado_exp.config(text=f"{r_exp_str} e^i {theta_str}π")

			# Coloca flechitas
			lcheck_pol.config(text='✔'); lcheck_bin.config(text='✔'); lcheck_exp.config(text='✔')

			# Grafica
			resultados_para_graficar = [(np.radians(res_pol[1]), res_pol[0])]
			graficar(resultados_para_graficar)


	# Si en la binómica pusieron x/0, se resetea por la indeterminación
	except ZeroDivisionError:
		## HOTFIX: Mostrar al usuario cuando mete algo inválido por división x/0
		lresultado_bin.configure(text="ERROR", fg=C_ERROR, font=("Microsoft Sans Serif", 16, "normal"))
		# esperar 3s para resetear
		root.after(3000, resetear)


# En sí es volver todo a su estado inicial
# Borrar variables
# Desactivar botones
# Recuperar el estilo inicial
def resetear():
	# Resetar variables y diseño
	global tipo1, tipo2, coperacion
	tipo1 = 0; tipo2 = 0; coperacion = 0
	show_standard_results_ui() 
	show_z2()

	# Borrar los formularios
	for entry in [entry_bin1_real, entry_bin1_imag, entry_pol1_mod, entry_pol1_arg, 
				  entry_exp1_mod, entry_exp1_num, entry_exp1_den, entry_bin2_real, 
				  entry_bin2_imag, entry_pol2_mod, entry_pol2_arg, entry_exp2_mod, 
				  entry_exp2_num, entry_exp2_den]:
		entry.delete(0, tk.END)
	
	#Diseño/quitar elementos
	_binomicas.grid_forget(); _polares.grid_forget(); _exponenciales.grid_forget()
	_binomicas1.grid_forget(); _polares1.grid_forget(); _exponenciales1.grid_forget()

	# Diseño/textos
	lz1.config(text='forma'); lz2.config(text='forma')
	loperacion.config(text='op')
	lresultado_pol.config(text=''); lresultado_bin.config(text=''); lresultado_exp.config(text='')
	lcheck_pol.config(text=''); lcheck_bin.config(text=''); lcheck_exp.config(text='')

	# Diseño/Desactivar botones
	suma.config(state=tk.DISABLED); resta.config(state=tk.DISABLED)
	multi.config(state=tk.DISABLED); divi.config(state=tk.DISABLED)
	potencia.config(state=tk.DISABLED); raiz.config(state=tk.DISABLED)
	conjugado.config(state=tk.DISABLED)

## HOTFIX: Vincular la tecla enter para calcular
root.bind('<Return>', lambda event: computar(tipo1, tipo2, coperacion))

## HOTFIX: Vincular teclas a operaciones

## Manejos especiales para suma y resta, si estoy enfocado en el entry no debe
## tratarlos como suma o resta, sino como signo ingresado en el entry
def foco_suma_resta(event, operation_id):
    focused_widget = root.focus_get()
    
    # Si estoy en entry, pon el signo
    if isinstance(focused_widget, tk.Entry):
        return

    # Si no, cambia la operación a suma/resta
    opera(operation_id)


# Cambia las operaciones
root.bind('+', lambda event: foco_suma_resta(event, 1)) # Suma
root.bind('-', lambda event: foco_suma_resta(event, 2)) # Resta
root.bind('*', lambda event: opera(3)) # Multiplicación
root.bind('/', lambda event: opera(4)) # División
root.bind('^', lambda event: opera_n(1)) # Potencia
root.bind('r', lambda event: opera_n(2)) # Raíz

# Resetea la calculadora
root.bind('<Control-BackSpace>', lambda event: resetear())

# Cambia el formato de z1
root.bind('<Control-KeyPress-1>', lambda event: set_z1_format(1)) # Binomial
root.bind('<Control-KeyPress-2>', lambda event: set_z1_format(2)) # Polar
root.bind('<Control-KeyPress-3>', lambda event: set_z1_format(3)) # Exponencial

# Cambia el formato de z2
root.bind('<Alt-KeyPress-1>', lambda event: set_z2_format(1)) # Binomial
root.bind('<Alt-KeyPress-2>', lambda event: set_z2_format(2)) # Polar
root.bind('<Alt-KeyPress-3>', lambda event: set_z2_format(3)) # Exponencial

# Iniciar con la UI de resultados estándar, el "main"
show_standard_results_ui()

# Función maestra de Tkinter
root.mainloop()