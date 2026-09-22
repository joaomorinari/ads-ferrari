n = int(input("Quantos casos voce vai digitar? "))

for i in range(n):
    num = int(input("Entre com o numerador: "))
    den = int(input("Entre com o denominador: "))
    if den == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        print(f"DIVISAO = {num / den:.2f}")