import re
import math
z = input("Ingrese un número complejo")

# binomica		"+/-i"
# polar			"cis"
# exponencial	"e^i"

# Expresiones regulares para validar el número complejo ingresado y procesarlo
regex_bin = r"(|\-)(\d+)(\+|\-)(\d+)i"
regex_pol = r"(|\-)(\d+)cis\((|\-)(\d+)°\)"
regex_exp = r"(|\-)(\d+)e\^i((|\-)(\d+)\/(|\-)(\d+)|(|\-)(\d+))pi"



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

		if re.search(regex_exp, z).group(4) == '-':
			a*= -1

		# denominador
		b = int(re.search(regex_exp, z).group(7))

		if re.search(regex_exp, z).group(6) == '-':
			a*= -1

		t = (math.pi)*(a/b)
		t%= math.tau
	else:
		t = math.pi*int(re.search(regex_exp, z).group(9))

		if re.search(regex_exp, z).group(8) == '-':
			t*=-1
		t%= math.tau
	return r,t

def validar(z):
	if re.search(regex_bin, z):
		return binomica(z)
	if re.search(regex_pol, z):
		print(re.findall(regex_pol, z))
		return polar(z)
	if re.search(regex_exp, z):
		return exponencial(z)
	else:
		return 0


print(validar(z))
