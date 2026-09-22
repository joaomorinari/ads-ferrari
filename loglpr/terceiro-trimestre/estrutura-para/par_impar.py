qtd = int(input("Quantos numeros você vai digitar? "))

for i in range(qtd):
    n = int(input("Digite um numero: "))

    if n == 0:
        print("NULO")
    else:
        status = "PAR" if n % 2 == 0 else "IMPAR"
        sinal = "POSITIVO" if n > 0 else "NEGATIVO"
        print(f"{status} {sinal}")