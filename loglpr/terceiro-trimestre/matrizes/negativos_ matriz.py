n = int(input("Qual o N de linhas da matriz ? "))
m = int(input("Qual o N de colunas da matriz? "))
matriz = []

for i in range(n):
    linha = []

    for j in range(m):
        elemento = int(input(f"Elemento [{i}, {j}]: "))
        linha.append(elemento)

    matriz.append(linha)

print("NUMEROS NEGATIVOS:")

for i in range(n):
    for j in range(m):
        if matriz[i][j] < 0:
            print(matriz[i][j])
            
