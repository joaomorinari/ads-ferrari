n = int(input("Qual a ordem da matriz? "))

matriz = []

for i in range(n):
	linha = []

	for j in range(n):
		elemento = int(input(f"Elemento [{i}, {j}]: "))
		linha.append(elemento)

	matriz.append(linha)

soma = 0

for i in range(n):
	for j in range(n):
		if j > i:
			soma += matriz[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")