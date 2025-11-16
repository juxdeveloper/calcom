import math

# Colocar ángulo en el intérvalo de trabajo
def fix_g(g):
    # Si g es mayor/menor al intérvalo de trabajo
    # Se resta o suma 360 hasta dar con un intérv.
    # dentro del mismo

    # Por ello podemos concluir que buscamos el
    # módulo, pues si son varias vueltas, después
    # de "descontarlas" obtenemos el residuo de
    # k vueltas
    return g%360

# Binómica --> Polar
def bin_pol(a,b,tipo=0):

    r = math.sqrt(a**2+b**2)

    ## HOTFIX: Si la parte real es 0, asignar el ángulo
    ## directamente para evitar dividir b/0
    ## [+] if b ...
    if a == 0:
        if b > 0:
            g = 90
        elif b < 0:
            g = 270
        else: # Origen (0,0)
            g = 0

    g = math.degrees(math.atan(b/a))
    # atan retorna de -90° a 90°

    if a < 0 and b > 0:  # 2do cuadrante
        g = 180+g
    elif a < 0 and b < 0: # 3er cuadrante
        g += 180
    elif a > 0 and b < 0: # 4to cuadrante
        g = 360+g

    return r,g

# Polar --> Exponencial
def pol_exp(r,g):
    t = math.radians(fix_g(g))/math.pi
    return r,t


# Exponencial --> Polar
def exp_pol(r,t):
    g = fix_g(math.degrees(t*math.pi))
    return r,g

# Polar --> Binomica
def pol_bin(r,g):
    a = r*math.cos(math.radians(fix_g(g)))
    b = r*math.sin(math.radians(fix_g(g)))
    return a,b

# Exponencial --> Binómica
def exp_bin(r,t):
    _polar = exp_pol(r,t)
    return pol_bin(_polar[0],_polar[1])