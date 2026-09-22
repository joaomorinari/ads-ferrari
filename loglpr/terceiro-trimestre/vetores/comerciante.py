nomes = []
compras = []
vendas = []
qtd = int(input("Serao digitados dados de quantos produtos? "))
for i in range(qtd):
    print("Produto {}:".format(i + 1))
    n = input("Nome: ")
    preco_compra = float(input("Preco de compra: "))
    preco_venda = float(input("Preco de venda: "))
    nomes.append(n)
    compras.append(preco_compra)
    vendas.append(preco_venda)

lucro_baixo = 0
lucro_medio = 0
lucro_alto = 0
for i in range(qtd):
    lucro = (vendas[i] - compras[i]) / compras[i] * 100
    if lucro < 10:
        lucro_baixo += 1
    elif lucro <= 20:
        lucro_medio += 1
    else:
        lucro_alto += 1

print("RELATORIO:")
print("Lucro abaixo de 10%: {}".format(lucro_baixo))
print("Lucro entre 10% e 20%: {}".format(lucro_medio))
print("Lucro acima de 20%: {}".format(lucro_alto))
print("Valor total de compra: {:.2f}".format(sum(compras)))
print("Valor total de venda: {:.2f}".format(sum(vendas)))
print("Lucro total: {:.2f}".format(sum(vendas) - sum(compras)))