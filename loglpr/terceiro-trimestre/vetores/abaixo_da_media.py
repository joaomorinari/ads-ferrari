vetor = []
qtd = int(input("Quantos elementos vai ter o vetor? "))
for i in range(qtd):
    n = float(input("Digite um numero: "))
    vetor.append(n)

media = sum(vetor) / qtd
print("MEDIA DO VETOR = {:.3f}".format(media))
print("ELEMENTOS ABAIXO DA MEDIA:")
for x in vetor:
    if x < media:
        print("{:.1f}".format(x))