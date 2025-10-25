import complexconv
import complexinput

def adicion(z1,z2,operacion=0):
    z1 = complexinput.ingresar(z1)
    z2 = complexinput.ingresar(z2)

    if complexinput.tipo(z1) == 1:
        complex.
    if complexinput.tipo(z1) == 2:
        complexconv.pol_bin(z1)
    elif complexinput.tipo(z1) == 3:
        complexconv.exp_bin(z1)

    if complexinput.tipo(z2) == 2:
        complexconv.pol_bin(z2)
    elif complexinput.tipo(z2) == 3:
        complexconv.exp_bin(z2)

# ChatGPT me ayudó a usar tuplas, pues no 
    # tenía idea de que tienen indices
    # sabiendo de su existencia, hice mi propio codigo
    if operacion == 0:
        resultado = (z1[0] + z2[0], z1[1] + z2[1])
    else:
        resultado = (z1[0] - z2[0], z1[1] - z2[1])
    return resultado

def factor(z1,z2,operacion=0):
    z1 = complexinput.ingresar(z1)
    z2 = complexinput.ingresar(z2)

    if complexinput.tipo(z1) == 1:
        complexconv.bin_pol(z1)
    elif complexinput.tipo(z1) == 3:
        complexconv.exp_pol(z1)

    if complexinput.tipo(z2) == 1:
        complexconv.bin_pol(z2)
    elif complexinput.tipo(z2) == 3:
        complexconv.exp_pol(z2)

    if operacion == 0:
        resultado = (z1[0]*z2[0],z1[1]+z2[1])
    else:
        resultado = (z1[0]/z2[0],z1[1]-z2[1])
        # fix later : indeteerminacion por 0
    return resultado

def potencia(z,n,operacion=0):
    z = complexinput.ingresar(z)

    if complexinput.tipo(z) == 1:
        z = complexconv.bin_pol(z)
    elif complexinput.tipo(z1) == 3:
        z = complexconv.exp_pol(z1)

    if operacion == 0:
        return z[0]**n,z[1]*n
        #return r**n,g*n
    else:
        soluciones = [] # se guardan las varias soluciones en una lista
        k = 0
        while(k < n):
            #p1 = r**(1/n)
            p1 = z[0]**(1/n)
            #p2 = (g+360*k)/n
            p2 = (z[1]+360*k)/n
            soluciones.append((p1,p2))
            k+=1
        return soluciones


# LEER README.MD
#o|b|p|e
#+| |b|b
#-| |b|b
#*|p| |p
#/|p| |p
#^|p| |p
#s|p| |p
