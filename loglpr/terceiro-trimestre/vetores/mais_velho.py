nomes = []
idades = []
qtd = int(input("Quantas pessoas voce vai digitar? "))
for i in range(qtd):
    print("Dados da {}a pessoa:".format(i + 1))
    n = input("Nome: ")
    idade = int(input("Idade: "))
    nomes.append(n)
    idades.append(idade)

maior_idade = max(idades)
pos = idades.index(maior_idade)
print("PESSOA MAIS VELHA: {}".format(nomes[pos]))