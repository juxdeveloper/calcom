import conv
#import cli

def operando_bin(tipo, a, b):
    if tipo == 1:
        return a,b # falta validar # cli.ingresar() --> binomica(z)
    elif tipo == 2:
        return conv.pol_bin(a,b)
    elif tipo == 3:
        return conv.exp_bin(a,b)

def operando_pol(tipo, a,b):
    if tipo == 2:
        return a,b
    elif tipo == 1:
        return conv.bin_pol(a,b)
    elif tipo == 3:
        return conv.exp_pol(a,b)

def adicion(tipo1,n1,n2,tipo2,n3,n4,operacion=0):

    z1 = operando_bin(tipo1, n1, n2)
    z2 = operando_bin(tipo2, n3, n4)

    if operacion == 0:
        resultado = (z1[0] + z2[0], z1[1] + z2[1])
    else:
        resultado = (z1[0] - z2[0], z1[1] - z2[1])
    return resultado

def factor(tipo1,n1,n2,tipo2,n3,n4,operacion=0):

    z1 = operando_pol(tipo1,n1,n2)
    z2 = operando_pol(tipo2,n3,n4)

    if operacion == 0:
        resultado = (z1[0]*z2[0],(z1[1]+z2[1])%360)
    else:
        resultado = (z1[0]/z2[0],(z1[1]-z2[1])%360)
        # fix later : indeteerminacion por 0
    return resultado

def potencia(tipo1,n1,n2,n,operacion=0):
    z = operando_pol(tipo1,n1,n2)

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