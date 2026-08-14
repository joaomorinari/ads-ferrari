salario = float(input("digite o valor do seu salario: "))


if salario <= 1000:
    acrecimo_percentual = 20
    valor_com_acrescimo = salario * (1 + acrecimo_percentual / 100)
    aumento = valor_com_acrescimo - salario


elif salario > 1000 and salario <= 3000:
    acrecimo_percentual = 15
    valor_com_acrescimo = salario * (1 + acrecimo_percentual / 100)
    aumento = valor_com_acrescimo - salario


elif salario > 3000 and salario <= 8000:
    acrecimo_percentual = 10
    valor_com_acrescimo = salario * (1 + acrecimo_percentual / 100)
    aumento = valor_com_acrescimo - salario


elif salario > 8000:
    acrecimo_percentual = 5
    valor_com_acrescimo = salario * (1 + acrecimo_percentual / 100)
    aumento = valor_com_acrescimo - salario


print(f"Seu novo salario é: R$ {valor_com_acrescimo:.2f}")
print(f"Seu aumento é de: R$ {aumento:.2f}")
print(f"Seu percentual de aumento: {acrecimo_percentual:.0f}%")