import conv
#import cli - Legacy

# Convertir a binómica para operaciones de suma-resta
def operando_bin(tipo, a, b):
    if tipo == 1:
        return a,b
    elif tipo == 2:
        return conv.pol_bin(a,b)
    elif tipo == 3:
        return conv.exp_bin(a,b)

# Convertir a polar para el resto de operaciones
def operando_pol(tipo, a,b):
    if tipo == 2:
        return a,b
    elif tipo == 1:
        return conv.bin_pol(a,b)
    elif tipo == 3:
        return conv.exp_pol(a,b)


# Operaciones de adición
def adicion(tipo1,n1,n2,tipo2,n3,n4,operacion=0):
    z1 = operando_bin(tipo1, n1, n2)
    z2 = operando_bin(tipo2, n3, n4)

    if operacion == 0:
        resultado = (z1[0] + z2[0], z1[1] + z2[1])
    else:
        resultado = (z1[0] - z2[0], z1[1] - z2[1])
    return resultado

# Operaciones de factores
def factor(tipo1,n1,n2,tipo2,n3,n4,operacion=0):

    z1 = operando_pol(tipo1,n1,n2)
    z2 = operando_pol(tipo2,n3,n4)

    if operacion == 0:
        resultado = (z1[0]*z2[0],(z1[1]+z2[1])%360)
    else:
        resultado = (z1[0]/z2[0],(z1[1]-z2[1])%360)
    return resultado

# Operaciones de potencias
def potencia(tipo1,n1,n2,n,operacion=0):
    z = operando_pol(tipo1,n1,n2)

    if operacion == 0:
        ## HOTFIX: Verificar el cuadrante
        ## [+] % 360
        return z[0]**n,z[1]*n % 360
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

# Operación del conjugado
def conjugado(tipo1,n1,n2):
    z = operando_bin(tipo1, n1,n2)
    a = z[0]
    b = z[1]
    return a,b*-1