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
