n = int(input("Qual a ordem da matriz? "))

matriz = []

for i in range(n):
	linha = []

	for j in range(n):
		elemento = float(input(f"Elemento [{i}, {j}]: "))
		linha.append(elemento)

	matriz.append(linha)

soma_positivos = 0

for i in range(n):
	for j in range(n):
		if matriz[i][j] > 0:
			soma_positivos += matriz[i][j]

print(f"SOMA DOS POSITIVOS: {soma_positivos}")

linha_escolhida = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA:")

for j in range(n):
	print(matriz[linha_escolhida][j])

coluna_escolhida = int(input("Escolha uma coluna: "))

print("COLUNA ESCOLHIDA:")

for i in range(n):
	print(matriz[i][coluna_escolhida])

print("DIAGONAL PRINCIPAL:")

for i in range(n):
	print(matriz[i][i])

for i in range(n):
	for j in range(n):
		if matriz[i][j] < 0:
			matriz[i][j] = matriz[i][j] ** 2

print("MATRIZ ALTERADA:")

for i in range(n):
	for j in range(n):
		print(matriz[i][j])