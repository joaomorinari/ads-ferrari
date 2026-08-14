preco_produto = float(input("digite o preco do produto: "))
quantidade = int(input("digite a quantidade comprada: "))
valor_recebido = float(input("digite o valor recebido: "))
total_compra = preco_produto * quantidade 
troco = valor_recebido - total_compra

if total_compra < valor_recebido:
    print(f"O troco é: {troco}")
elif total_compra > valor_recebido:
    print("dinheiro insuficiente.")
else:
    print("Não tem troco.")
    