import complexconv
import complexinput

def adicion(z1,z2,operacion=0):

    if complexinput.tipo(z1) == 1:
        z1 = complexinput.ingresar(z1,1)
    elif complexinput.tipo(z1) == 2:
        z1 = complexinput.ingresar(z1,2)
        z1 = complexconv.pol_bin(z1[0],z1[1])
    elif complexinput.tipo(z1) == 3:
        z1 = complexinput.ingresar(z1,2)
        z1 = complexconv.pol_bin(z1[0],z1[1])

    if complexinput.tipo(z2) == 1:
        z2 = complexinput.ingresar(z2,1)
    elif complexinput.tipo(z2) == 2:
        z2 = complexinput.ingresar(z2,2)
        z2 = complexconv.pol_bin(z2[0],z2[1])
    elif complexinput.tipo(z2) == 3:
        z2 = complexinput.ingresar(z2,2)
        z2 = complexconv.pol_bin(z2[0],z2[1])

# ChatGPT me ayudó a usar tuplas, pues no 
    # tenía idea de que tienen indices
    # sabiendo de su existencia, hice mi propio codigo
    if operacion == 0:
        resultado = (z1[0] + z2[0], z1[1] + z2[1])
    else:
        resultado = (z1[0] - z2[0], z1[1] - z2[1])
    return resultado

def factor(z1,z2,operacion=0):

    if complexinput.tipo(z1) == 2:
        z1 = complexinput.ingresar(z1,2)
    elif complexinput.tipo(z1) == 1:
        z1 = complexinput.ingresar(z1,1)
        z1 = complexconv.bin_pol(z1[0],z1[1])
    elif complexinput.tipo(z1) == 3:
        z1 = complexinput.ingresar(z1,3)
        z1 = complexconv.exp_pol(z1[0],z1[1])

    if complexinput.tipo(z2) == 2:
        z2 = complexinput.ingresar(z2,2)
    elif complexinput.tipo(z2) == 1:
        z2 = complexinput.ingresar(z2,1)
        z2 = complexconv.bin_pol(z2[0],z2[1])
    elif complexinput.tipo(z2) == 3:
        z2 = complexinput.ingresar(z2,3)
        z2 = complexconv.exp_pol(z2[0],z2[1])

    if operacion == 0:
        resultado = (z1[0]*z2[0],(z1[1]+z2[1])%360)
    else:
        resultado = (z1[0]/z2[0],(z1[1]-z2[1])%360)
        # fix later : indeteerminacion por 0
    return resultado

def potencia(z,n,operacion=0):
    if complexinput.tipo(z) == 2:
        z = complexinput.ingresar(z,2)
    elif complexinput.tipo(z) == 1:
        z = complexinput.ingresar(z,1)
        z = complexconv.bin_pol(z[0],z[1])
    elif complexinput.tipo(z) == 3:
        z = complexinput.ingresar(z,3)
        z = complexconv.exp_pol(z[0],z[1])

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
