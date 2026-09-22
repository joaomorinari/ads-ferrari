numeros = []
qtd = int(input("Quanto numeros voce vai digitar? "))
for i in range(qtd):
    n = float(input("Digite um numero: "))
    numeros.append(n)

maior = max(numeros)
pos = numeros.index(maior)
print("MAIOR VALOR = {}".format(maior))
print("POSICAO DO MAIOR VALOR = {}".format(pos))