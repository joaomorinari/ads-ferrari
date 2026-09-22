numeros = []
qtd = int(input("Quantos numeros voce vai digitar? "))
for i in range(qtd):
    n = int(input("Digite um numero: "))
    numeros.append(n)

pares = [x for x in numeros if x % 2 == 0]
print("NUMEROS PARES:")
print(" ".join(str(x) for x in pares))
print("QUANTIDADE DE PARES = {}".format(len(pares)))