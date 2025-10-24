import math
from fractions import Fraction

# CONVERTIDOR ESTÁNDAR DE NÚMEROS COMPLEJOS
# EN TODAS SUS FORMAS


# Binómica --> Polar
def bin_pol(a,b,tipo=0):
    if tipo == 0:
        r = math.sqrt(a**2+b**2)
        t = math.atan(b/a)
        g = math.degrees(t)
        return r,g
    else:
        r = math.sqrt(a**2+b**2)
        t = (math.atan(b/a))/math.pi
        return r,t

# Polar --> Exponencial
def pol_exp(a,b):
    r = a
    t = math.radians(b)/math.pi
    return r,t
print(pol_exp(2,60))
