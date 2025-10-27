import re
import math

# Colores en la terminal para dar formato
# (Copiado de StackOverflow https://v.gd/fXwn3b)
def cl(color=0):
	print('\033[1m', end='')
	match color:
		case 'r':
			print('\033[91m', end='')
		case 'g':
			print('\033[92m', end='')
		case 'b':
			print('\033[94m', end='')
		case 'y':
			print('\033[93m', end='')
		case 0:
			print('\033[0m', end='')

# Patrones característicos de cada tipo de número complejo

# binomica		"+/-i"
# polar			"cis"
# exponencial	"e^i"

# Expresiones regulares para validar el número complejo ingresado y procesarlo
regex_bin = r"(|\-)(\d+)(\+|\-)(\d+)i"
regex_pol = r"(|\-)(\d+)cis\((|\-)(\d+)°\)"
regex_exp = r"(|\-)(\d+)e\^i((|\-)(\d+)\/(|\-)(\d+)|(|\-)(\d+))pi"

# ===========================================
# BINÓMICA
# ===========================================
#regex_bin = r"(|\-)(\d+)(\+|\-)(\d+)i"
def binomica(z):
	# asignacion de a
	a = int(re.search(regex_bin, z).group(2))

	# signo de a
	if re.search(regex_bin, z).group(1) == '-':
		a*= -1

	# asignacion de b
	b = int(re.search(regex_bin, z).group(4))

	# signo de b
	if re.search(regex_bin, z).group(3) == '-':
		b*=-1
	return a,b

# ===========================================
# POLAR
# ===========================================
# regex_pol = r"(|\-)(\d+)cis\((|\-)(\d+)°\)"
def polar(z):
	# modulo
	r = int(re.search(regex_pol, z).group(2))

	# signo de modulo
	if re.search(regex_pol, z).group(1) == '-':
		r*= -1

	# angulo
	g = int(re.search(regex_pol, z).group(4))

	# signo de angulo
	if re.search(regex_pol, z).group(3) == '-':
		g*= -1

	# angulo de trabajo
	g%=360
	return r,g


# ===========================================
# EXPONENCIAL
# ===========================================
# regex_exp = r"(|\-)(\d+)e\^i((|\-)(\d+)\/(|\-)(\d+)|(|\-)(\d+))pi"
#                (g1)(g2)::g3:: :g4:(g5)(g6)(g7)(g8) :g9:(g10)(g11)
#  g1: signo modulo
#  g2: modulo

#  g3: fraccion/numero de pi*rad
		#  g4: signo de numerador
		#  g5: numerador
		#  g6: signo de denominador
		#  g7: denominador
		
		#  g8: signo de numero
		#  g9: numero

def exponencial(z):
	# modulo
	r = int(re.search(regex_exp, z).group(2))

	# signo de modulo
	if re.search(regex_exp, z).group(1) == '-':
		r*= -1

	# fraccion/numero de pi*rad
	if '/' in re.search(regex_exp, z).group(3):
		# numerador
		a = int(re.search(regex_exp, z).group(5))

		# signo
		if re.search(regex_exp, z).group(4) == '-':
			a*= -1

		# denominador
		b = int(re.search(regex_exp, z).group(7))

		# signo
		if re.search(regex_exp, z).group(6) == '-':
			a*= -1

		# DENOMINADOR b NO DEBE SER 0
		t = (math.pi)*(a/b)
		t%= math.tau
	else:
		t = math.pi*int(re.search(regex_exp, z).group(9))

		if re.search(regex_exp, z).group(8) == '-':
			t*=-1
		t%= math.tau
	return r,t

# Retorna el tipo de expresión
def tipo(z):
	if re.search(regex_bin, z):
		return 1
	if re.search(regex_pol, z):
		return 2
	if re.search(regex_exp, z):
		return 3
	else:
		return 0

# Imprime el tipo de expresión
def imprimir_tipo(z,n=0):
    print("z" + str(n) + " es ", end="")
    match tipo(z):
        case 1:
            print("BINÓMICA")
        case 2:
            print("POLAR")
        case 3:
            print("EXPONENCIAL")

# Ingresa/parsea la expresión
def ingresar(z,tipo):
	match tipo:
		case 1:
			return binomica(z)
		case 2:
			return polar(z)
		case 3:
			return exponencial(z)
		case _:
			return 0