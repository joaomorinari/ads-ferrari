condicao = True

while condicao:
    valor_x= int(input("Digite o valor da coordenada X: "))
    valor_y= int(input("Digite o valor da coordenada Y: "))

    if valor_x > 0 and valor_y > 0:
            print("Q1")
    elif valor_x < 0 and valor_y > 0:
            print("Q2")
    elif valor_x < 0 and valor_y < 0:
            print("Q3")
    elif valor_x > 0 and valor_y < 0:
            print("Q4")
    else:
        condicao = False
