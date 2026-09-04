A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A > B:
    X = A
    A = B
    B = X

if A > C:
    X = A
    A = C
    C = X

if B > C:
    X = B
    B = C
    C = X

print("A =", A)
print("B =", B)
print("C =", C)