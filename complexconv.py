import math

def fix_g(g):
    # Si g es mayor/menor al intérvalo de trabajo
    # Se resta o suma 360 hasta dar con un intérv.
    # dentro del mismo

    # Por ello podemos concluir que buscamos el
    # módulo, pues si son varias vueltas, después
    # de "descontarlas" obtenemos el residuo de
    # k vueltas
    return g%360


# CONVERTIDOR ESTÁNDAR DE NÚMEROS COMPLEJOS
# EN TODAS SUS FORMAS

#bin_pol    <-->    pol_bin
#pol_exp    <-->    exp_pol

# VARIABLES
# a y b     : términos binómicos
# g         : ángulo en grados
# t         : ángulo en radianes
# Binómica --> Polar
def bin_pol(a,b,tipo=0):
    r = math.sqrt(a**2+b**2)
    if a == 0:
        return r,0

    g = math.degrees(math.atan(b/a))

    if a < 0 and b > 0:  # 2do cuadrante
        g = 180+g
    elif a < 0 and b < 0: # 3er cuadrante
        g += 180
    elif a > 0 and b < 0: # 4to cuadrante
        g = 360+g

    if tipo == 0:
        return r,g
    else:
        t = (math.radians(g))/math.pi
        return r,t

# Polar --> Exponencial
# T1 : g debe estar [0-359]
def pol_exp(r,g):
    t = math.radians(fix_g(g))/math.pi
    return r,t


# Exponencial --> Polar
# R1 : g debe estar [0-359], código redundante
# con lo de arriba
def exp_pol(r,t):
    g = fix_g(math.degrees(t*math.pi))
    return r,g

# Polar --> Binomica
# R1 : g debe estar [0-359], código redundante
def pol_bin(r,g):
    a = r*math.cos(math.radians(fix_g(g)))
    b = r*math.sin(math.radians(fix_g(g)))
    return a,b

def exp_bin(r,t):
    _polar = exp_pol(r,t)
    return pol_bin(_polar[0],_polar[1])

### ===== DEMOS ===== ###
# binómica --> polar
#print(bin_pol(3,4))
#print(bin_pol(-3,4))
#print(bin_pol(-3,-4))
#print(bin_pol(3,-4))

# polar --> binómica
#print(pol_bin(5,53.13010235415598))
#print(pol_bin(5, 126.86989764584402))
#print(pol_bin(5, 233.13010235415598))
#print(pol_bin(5, 306.86989764584405))

# polar --> exponencial
#print(pol_exp(3,45))
#print(pol_exp(3,135))
#print(pol_exp(3,225))
#print(pol_exp(3,315))

# exponencial --> polar
#print(exp_pol(3, 0.25))
#print(exp_pol(3, 0.75))
#print(exp_pol(3, 1.25))
#prrint(exp_pol(3, 1.75))

# Indeterminaciones / Búsqueda de errores
#print(pol_exp(3,495))
#print(exp_pol(3,0.75))
#print(pol_bin(3,495))
#print(bin_pol(-2.1213203435596424, 2.121320343559643))

# En la 3ra versión, concluyo con un programa robusto, docmuentado y fácil de leer / depurar
