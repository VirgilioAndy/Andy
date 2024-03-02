def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, None

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    valor_a_buscar = 5

    encontrado, posicion = buscar_en_matriz(matriz, valor_a_buscar)

    if encontrado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()

s