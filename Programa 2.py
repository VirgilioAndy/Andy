def ordenar_fila_en_matriz(matriz, fila):
    # Selecciona la fila específica de la matriz
    fila_a_ordenar = matriz[fila]

    # Implementa el algoritmo de ordenación de burbuja
    n = len(fila_a_ordenar)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    matriz = [
        [3, 2, 1],
        [6, 5, 4],
        [9, 8, 7]
    ]
    fila_a_ordenar = 1  # Selecciona la fila a ordenar (0-indexada)

    print("Matriz original:")
    imprimir_matriz(matriz)

    ordenar_fila_en_matriz(matriz, fila_a_ordenar)

    print("\nMatriz con la fila ordenada:")
    imprimir_matriz(matriz)

if __name__ == "__main__":
    main()
