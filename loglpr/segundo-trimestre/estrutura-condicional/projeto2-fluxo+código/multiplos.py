A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))

if A % B == 0 or B % A == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")