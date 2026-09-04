valor_1 = int(input("digite o primeiro valor: "))
valor_2 = int(input("digite o segundo valor: "))
valor_3 = int(input("digite o terceiro valor: "))

if valor_1 < valor_2 < valor_3:
    print(f"Menor: {valor_1}")

elif valor_2 < valor_3 < valor_1:
    print(f"Menor: {valor_2}")

elif valor_3 < valor_2 < valor_1:
    print(f"Menor: {valor_3}")
