vetor = []
qtd = int(input("Quantos numeros voce vai digitar? "))
for i in range(qtd):
    n = float(input("Digite um numero: "))
    vetor.append(n)

soma = sum(vetor)
media = soma / qtd

print("VALORES =", " ".join(str(x) for x in vetor))
print("SOMA = {:.2f}".format(soma))
print("MEDIA = {:.2f}".format(media))