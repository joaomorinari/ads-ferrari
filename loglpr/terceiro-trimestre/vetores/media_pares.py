numeros = []
qtd = int(input("Quantos elementos vai ter o vetor? "))
for i in range(qtd):
    n = int(input("Digite um numero: "))
    numeros.append(n)

pares = [x for x in numeros if x % 2 == 0]
if len(pares) == 0:
    print("NENHUM NUMERO PAR")
else:
    media = sum(pares) / len(pares)
    print("MEDIA DOS PARES = {:.1f}".format(media))