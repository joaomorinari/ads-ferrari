preco = float(input("Preco unitario do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

total = preco * quantidade
troco = dinheiro - total

print(f"TROCO = {troco:.2f}")