n = int(input("Qual a ordem da matriz? "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        elemento = int(input(f"Elemento [{i}, {j}]: "))
        linha.append(elemento)

    matriz.append(linha)

contador = 0

print("DIAGONAL PRINCIPAL:")

for i in range(n):
    print(matriz[i][i])

for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            contador += 1

print(f"Total de negativos: {contador}")