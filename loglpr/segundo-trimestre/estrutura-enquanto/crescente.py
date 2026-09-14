condicao = True

while condicao:
    valor1 = int(input("Digite um numero: "))
    valor2 = int(input("Digite outro numero: "))

    if valor1 != valor2:
        if valor1 < valor2:
            print("crescente")
        else:
            print("decrescente")
        if valor1 == valor2:
         condicao = False
    
