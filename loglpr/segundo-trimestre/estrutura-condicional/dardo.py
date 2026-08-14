valor_1 = float(input("digite a primeira distancia: "))
valor_2 = float(input("digite a segunda distancia "))
valor_3 = float(input("digite a terceira distancia: "))

if valor_1 > valor_2 > valor_3:
    print(f"Maior: {valor_1}")

if valor_2 > valor_3 > valor_1:
    print(f"Maior: {valor_2}")

if valor_3 > valor_2 > valor_1:
    print(f"Maior: {valor_3}")

