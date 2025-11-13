# calcom
A robust, simple, beautiful Calculator for Complex numbers

# Lógica de operaciones
*   La primera fila representa la forma a operar.
*   Si la forma es nativa (se opera sin convertir), la celda está vacía.
*   De lo contrario, la celda indica la forma a la que se debe convertir el número para ser operado. La siguiente tabla resume esta lógica:

| Operación      | Binómica | Polar  | Exponencial |
|----------------|:--------:|:------:|:-----------:|
| Suma           |          |Binómica| Binómica    |
| Resta          |          |Binómica| Binómica    |
| Multiplicación | Polar    |        | Polar       |
| División       | Polar    |        | Polar       |
| Potencia       | Polar    |        | Polar       |
| Raíz n-ésima   | Polar    |        | Polar       |

# Documentación de los programas

## 📄 `cli.py`
```python
import cli
```
> UTILIDAD ESTÁNDAR PARA INGRESO Y MANEJO DE DATOS EN LA TERMINAL

### Funciones Notables

*   `tipo(z)`: Obtiene el tipo de expresión.
    *   **Retorna**: `[0=error, 1=bin, 2=pol, 3=exp]`

*   `imprimir_tipo(z, n=0)`: Imprime el tipo de expresión y su número.
    *   **Retorna**: `void`

*   `ingresar(z, tipo)`: Obtiene la expresión en variables operables.
    *   **Retorna**:
        *   `a,b` = bin
        *   `r,g` = pol
        *   `r,t` = exp

*   `cl(color)`: Formatea la terminal en distintos colores.
    *   **Retorna**: `void`
    *   **Colores**:
        *   `'r'` = red
        *   `'g'` = green
        *   `'b'` = blue
        *   `'y'` = yellow
        *   `0` = reset

---

## 📄 `conv.py`
```python
import conv
```
> CONVERTIDOR ESTÁNDAR DE NÚMEROS COMPLEJOS EN TODAS SUS FORMAS

`bin_pol` <--> `pol_bin`  
`pol_exp` <--> `exp_pol`

### Variables Constantes
*   **a y b**: términos binómicos
*   **g**: ángulo en grados
*   **t**: ángulo en radianes

### Nombre de Funciones
La nomenclatura sigue el formato `source_objetive` (`sou_obj`).
*   3 letras de abreviatura de la fuente + `_` + abreviatura del objetivo.

### Abreviaturas
1.  `bin` (binómica)
2.  `pol` (polar)
3.  `exp` (exponencial)

---

## 📄 `operations.py`
```python
import operations
```
> CALCULADORA ESTÁNDAR PARA TODAS LAS OPERACIONES

### Parámetros
*   `z1`: 1er número complejo
*   `z2`: 2do número complejo
*   `operacion`: Define la operación específica (ej. suma o resta)

### Funciones Notables
*   `adicion(z1, z2, operacion=0)`: Realiza suma o resta.
    *   **Return**: `a,b` (forma bin)

*   `factor(z1, z2, operacion=0)`: Realiza multiplicación o división.
    *   **Return**: `r,g` (forma pol)

*   `potencia(z1, n, operacion=0)`: Realiza potencia o raíz.
    *   **Return**: `r,g` (forma pol)

*   `conjugado(z1)`: Realiza potencia o raíz.
    *   **Return**: `a,b` (forma bin)
*Formato markdown por Gemini ✨*

*Hecho con 🚀 (ambición) por Joseph*
