import math
from fractions import Fraction

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
    if tipo == 0:
        g = math.degrees(math.atan(b/a))
        if a < 0 and b > 0:  # 2do cuadrante
            g = 180+g
        elif a < 0 and b < 0: # 3er cuadrante
            g += 180
        elif a > 0 and b < 0: # 4to cuadrante
            g = 360+g
        return r,g
    else:
        t = (math.atan(b/a))/math.pi
        return r,t

# Polar --> Exponencial
def pol_exp(r,g):
    t = math.radians(g)/math.pi
    return r,t


# Exponencial --> Polar
def exp_pol(r,t):
    g = math.degrees(t*math.pi)
    while g < 0:
        g+=360
    while g >= 360:
        g-=360
    return r,g

# Polar --> Binomica
def pol_bin(r,g):
    a = r*math.cos(math.radians(g))
    b = r*math.sin(math.radians(g))
    return a,b

# DEMO
# binómica --> polar
print(bin_pol(3,4))
print(bin_pol(-3,4))
print(bin_pol(-3,-4))
print(bin_pol(3,-4))

# polar --> binómica
print(pol_bin(5,53.13010235415598))
print(pol_bin(5, 126.86989764584402))
print(pol_bin(5, 233.13010235415598))
print(pol_bin(5, 306.86989764584405))

# polar --> exponencial
print(pol_exp(3,45))
print(pol_exp(3,135))
print(pol_exp(3,225))
print(pol_exp(3,315))

# exponencial --> polar
print(exp_pol(3, 0.25))
print(exp_pol(3, 0.75))
print(exp_pol(3, 1.25))
print(exp_pol(3, 1.75))
