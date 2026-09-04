minutos = int(input("digite a quantidade de minutos: "))

if minutos <= 100:
    valor = 50

else:
    minutos_excedentes = minutos - 100
    valor = 50 + (minutos_excedentes * 2)

print(f"Valor a pagar: R$ {valor:.2f}")