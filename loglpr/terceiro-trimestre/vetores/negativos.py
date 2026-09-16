numeros = []
qtd = int(input("quantos numeros vai digitar?"))
for i in range(qtd):
    n = int(input("digite um numero: "))
    numeros.append(n)

print("Numeros negativos: ")
for numero in numeros:
    if numero < 0:
        print(numero)


