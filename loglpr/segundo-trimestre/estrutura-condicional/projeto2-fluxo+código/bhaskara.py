valor_a = float(input("digite o primeiro valor"))
valor_b = float(input("digite o segundo valor"))
valor_c = float(input("digite o terceiro valor"))

delta = valor_b ** 2 - 4 * valor_a * valor_c

if delta < 0:
    print("Esta equação não possui raízes reais")

    valor_a = float(input("digite o primeiro valor"))
valor_b = float(input("digite o segundo valor"))
valor_c = float(input("digite o terceiro valor"))

delta = valor_b ** 2 - 4 * valor_a * valor_c

if delta < 0:
    print("Esta equação não possui raízes reais")
else:
    x1 = (-valor_b + delta ** 0.5) / (2 * valor_a)
    x2 = (-valor_b - delta ** 0.5) / (2 * valor_a)

    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")