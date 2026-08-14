compra = int(input("digite o código do produto comprado: "))
quantidade = int(input("digite a quantidade comprada: "))
if compra == 1:
    preco = 5.00

elif compra == 2:
    preco = 3.50

elif compra == 3:
    preco = 4.80

elif compra == 4:
    preco = 8.90

elif compra == 5:
    preco = 7.32

else:
    print("opçao inválida!")

total = preco * quantidade

print(f"Valor a pagar: R${total:.2f}")
