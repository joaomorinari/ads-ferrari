qtd = int(input("Quantos valores vai ter cada vetor? "))
a = []
b = []
print("Digite os valores do vetor A:")
for i in range(qtd):
    n = int(input())
    a.append(n)
print("Digite os valores do vetor B:")
for i in range(qtd):
    n = int(input())
    b.append(n)

c = []
for i in range(qtd):
    c.append(a[i] + b[i])

print("VETOR RESULTANTE:")
for x in c:
    print(x)