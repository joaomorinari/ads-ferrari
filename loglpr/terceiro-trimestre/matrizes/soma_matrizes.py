qtd_linhas = int(input("Quantas linhas vai ter cada matriz? "))
qtd_colunas = int(input("Quantas colunas vai ter cada matriz? "))

matrizA = []
matrizB = []

print("Digite os valores da matriz A:")

for i in range(qtd_linhas):
	linha = []

	for j in range(qtd_colunas):
		elemento = int(input(f"Elemento [{i}, {j}]: "))
		linha.append(elemento)

	matrizA.append(linha)

print("Digite os valores da matriz B:")

for i in range(qtd_linhas):
	linha = []

	for j in range(qtd_colunas):
		elemento = int(input(f"Elemento [{i}, {j}]: "))
		linha.append(elemento)

	matrizB.append(linha)

matrizC = []

for i in range(qtd_linhas):
	linhaC = []

	for j in range(qtd_colunas):
		soma = matrizA[i][j] + matrizB[i][j]
		linhaC.append(soma)

	matrizC.append(linhaC)

print("MATRIZ SOMA:")

for i in range(qtd_linhas):
	for j in range(qtd_colunas):
		print(matrizC[i][j])