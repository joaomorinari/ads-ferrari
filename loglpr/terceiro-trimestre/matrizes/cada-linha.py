N = int(input("qual a ordem da matriz? "))

matriz = []
for i in range(N):
	linha = []
	for j in range(N):
		valor = int(input(f"elemento [{i},{j}]: "))
		linha.append(valor)
	matriz.append(linha)

for linha in matriz:
	print(max(linha))
