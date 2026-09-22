n = int(input("Quantos numeros voce vai digitar? "))
dentro = 0

for i in range(n):
    x = int(input("Digite um numero: "))
    if x >= 10 and x <= 20:
        dentro += 1

fora = n - dentro
print(f"{dentro} DENTRO")
print(f"{fora} FORA")