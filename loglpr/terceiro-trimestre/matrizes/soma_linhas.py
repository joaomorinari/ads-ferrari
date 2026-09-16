qtd_linhas = int(input("Digite a quantidade de linhas: "))
qtd_colunas = int(input("Digite a quantidade de colunas: "))

matriz = []
vetor = []

for x in range(1, qtd_linhas + 1):
    linha = []

    print(f"Digite os elementos da {x}ª linha:")

    for y in range(1, qtd_colunas + 1):
        elemento = float(input())
        linha.append(elemento)

    matriz.append(linha)

for linha in matriz:
    soma = 0

    for elemento in linha:
        soma += elemento

    vetor.append(soma)

print("VETOR GERADO:")

for soma in vetor:
    print(soma)