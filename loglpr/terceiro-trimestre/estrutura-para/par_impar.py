qtd = int(input("Quantos numeros você vai digitar? "))

for i in range(qtd):
    n = int(input("Digite um numero: "))

    if n == 0:
        print("NULO")
    elif n % 2 == 0 and n > 0:
        print("PAR POSITIVO")
    elif n % 2 == 0 and n < 0:
        print("PAR NEGATIVO")
    elif n % 2 != 0 and n > 0:
        print("IMPAR POSITIVO")
    else:
        print("IMPAR NEGATIVO")