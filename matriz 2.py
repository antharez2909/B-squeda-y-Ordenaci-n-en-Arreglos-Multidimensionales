# Definición de la matriz bidimensional (3x3)
matriz = [
    [7, 3, 5],
    [4, 1, 3],
    [2, 8, 9]
]

# Función para ordenar una fila específica utilizando Bubble Sort
def ordenar_fila(matriz, fila_index):
    # Obtener la fila específica de la matriz
    fila = matriz[fila_index]

    # Aplicar Bubble Sort a la fila
    n = len(fila)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    # Actualizar la matriz con la fila ordenada
    matriz[fila_index] = fila

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir el índice de la fila a ordenar
fila_a_ordenar = 1  # Puedes cambiar este índice para ordenar una fila diferente (0, 1 o 2)

# Ordenar la fila específica de la matriz
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)