n = int(input("Quantos casos de teste serao digitados? "))
coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    qtd = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia: ")
    if tipo == "C":
        coelhos += qtd
    elif tipo == "R":
        ratos += qtd
    else:
        sapos += qtd

total = coelhos + ratos + sapos
print("RELATORIO FINAL:")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos * 100 / total:.2f}")
print(f"Percentual de ratos: {ratos * 100 / total:.2f}")
print(f"Percentual de sapos: {sapos * 100 / total:.2f}")