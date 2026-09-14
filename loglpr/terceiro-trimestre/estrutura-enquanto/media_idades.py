condicao = True
soma = 0
quantidade = 0
while condicao:
    idade = int(input("Digite a idade: "))
    if idade < 0:
        print("Idade inválida.")
        condicao = False
    else: 
        soma += idade
        quantidade += 1

if quantidade == 0:
    print("IMPOSSIVEL CALCULAR ")

else:
    media = soma / quantidade
    print(f"A média das idades é: {media:.2f}")

    