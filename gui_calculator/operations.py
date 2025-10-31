import conv
import cli

def operando_bin(z):
    tipo_z = cli.tipo(z)

    if tipo_z == 1:
        return cli.ingresar(z,1)
    elif tipo_z == 2:
        z = cli.ingresar(z,2)
        return conv.pol_bin(z[0],z[1])
    elif tipo_z == 3:
        z = cli.ingresar(z,3)
        return conv.exp_bin(z[0],z[1])

def operando_pol(z):
    tipo_z = cli.tipo(z)

    if tipo_z == 2:
        return cli.ingresar(z,2)
    elif tipo_z == 1:
        z = cli.ingresar(z,1)
        return conv.bin_pol(z[0],z[1])
    elif tipo_z == 3:
        z = cli.ingresar(z,3)
        return conv.exp_pol(z[0],z[1])

def adicion(z1,z2,operacion=0):

    z1 = operando_bin(z1)
    z2 = operando_bin(z2)

    # ChatGPT me ayudó a usar tuplas, pues no 
    # tenía idea de que tienen indices
    # sabiendo de su existencia, hice mi propio codigo
    if operacion == 0:
        resultado = (z1[0] + z2[0], z1[1] + z2[1])
    else:
        resultado = (z1[0] - z2[0], z1[1] - z2[1])
    return resultado

def factor(z1,z2,operacion=0):

    z1 = operando_pol(z1)
    z2 = operando_pol(z2)

    if operacion == 0:
        resultado = (z1[0]*z2[0],(z1[1]+z2[1])%360)
    else:
        resultado = (z1[0]/z2[0],(z1[1]-z2[1])%360)
        # fix later : indeteerminacion por 0
    return resultado

def potencia(z,n,operacion=0):
    z = operando_pol(z)

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