senha = 2002
condicao = True
while condicao:
    senha_digitada = int(input("Digite a senha: "))
    if senha_digitada == senha:
        print("Acesso permitido!")
        condicao = False
    else:
        print("Senha invalida! Tente novamente.")