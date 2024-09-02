# Matriz bidimensional (3x3)
matriz = [
    [7, 3, 5],
    [4, 1, 3],
    [2, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición (fila, columna) si se encuentra el valor
    return None  # Retorna None si no se encuentra el valor

# Definir el valor a buscar
valor_buscado = 5

# Verificar si el valor se encuentra en la matriz usando la función buscar_valor
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado de la búsqueda
if posicion:
    print(f"Se encontró el valor {valor_buscado} en la posición (fila: {posicion[0]}, columna: {posicion[1]}) de la matriz.")
else:
    print(f"No se encontró el valor {valor_buscado} en la matriz.")