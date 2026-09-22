nomes = []
notas1 = []
notas2 = []
qtd = int(input("Quantos alunos serao digitados? "))
for i in range(qtd):
    print("Digite nome, primeira e segunda nota do {}o aluno:".format(i + 1))
    n = input()
    n1 = float(input())
    n2 = float(input())
    nomes.append(n)
    notas1.append(n1)
    notas2.append(n2)

print("Alunos aprovados:")
for i in range(qtd):
    media = (notas1[i] + notas2[i]) / 2
    if media >= 6.0:
        print(nomes[i])