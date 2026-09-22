alturas = []
generos = []
qtd = int(input("Quantas pessoas serao digitadas? "))
for i in range(qtd):
    alt = float(input("Altura da {}a pessoa: ".format(i + 1)))
    gen = input("Genero da {}a pessoa: ".format(i + 1))
    alturas.append(alt)
    generos.append(gen)

alt_mulheres = [alturas[i] for i in range(qtd) if generos[i] == "F"]
media_mulheres = sum(alt_mulheres) / len(alt_mulheres)
print("Menor altura = {:.2f}".format(min(alturas)))
print("Maior altura = {:.2f}".format(max(alturas)))
print("Media das alturas das mulheres = {:.2f}".format(media_mulheres))
print("Numero de homens = {}".format(generos.count("M")))