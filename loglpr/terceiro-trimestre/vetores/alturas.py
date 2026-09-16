pessoas = []
qtd = int(input("quantas pessoas vai digitar?"))
for i in range(qtd):
    print("Dados da {}ª pessoa:".format(i + 1))
    n = (input("nome: "))
    idade = int(input("idade: "))
    altura = float(input("altura: "))
    pessoas.append((n, idade, altura))

media_altura = sum(p[2] for p in pessoas) / qtd
print("Altura média: {:.2f}".format(media_altura))

menores_16 = [p[0] for p in pessoas if p[1] < 16]
porcentagem = (len(menores_16) / qtd) * 100

print("\nPessoas com menos de 16 anos: {:.1f}%".format(porcentagem))
for nome in menores_16:
    print(f"- {nome}")


