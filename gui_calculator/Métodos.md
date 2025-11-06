BOTÓN
binomica,polar,exponencial
Presionar para seleccionar tipo de número complejo

LABEL
lz1,lz2
Imprime el tipo de número complejo seleccionado

FRAME
_binomicas, _polares, _exponenciales_
Invoca el formulario de cada tipo de número complejo

GRAPH
n/d
Actualizar gráfica


-----> Confirma entrada <-----
BOTÓN 
potencia,raiz,multi,divi,suma,resta
Presionar para seleccionar operación

LABEL
loperacion
Imprime la operación seleccionada

			###################################
			SI LA OPERACIÓN ES POTENCIA O RAIZ:
			###################################
			SPINBOX
			nspin
			Permite establecer el exponente o índice de la potencia o raíz respectivamente

			LABEL
			ntext
			Acompaña a nspin para facilitar la entrada al usuario


###################################
REPITE 1-4 PARA z2
###################################


-----> Confirma entrada <-----
BOTÓN
equal
Presionar para obtener resultado

LABEL
lresultado
Imprime el resultado de la operación

GRAPH
n/d
Actualizar gráfica








a1,b1
rp1,g1
re1,t1_1,t2_1


a2,b2
rp2,g2
re2,t1_2,t2_2