A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))
D = int(input("Digite D: "))

Resto2 = A % 2
Resto3 = A % 3

if Resto2 == 0 and Resto3 == 0:
    print(A)

Resto2 = B % 2
Resto3 = B % 3

if Resto2 == 0 and Resto3 == 0:
    print(B)

Resto2 = C % 2
Resto3 = C % 3

if Resto2 == 0 and Resto3 == 0:
    print(C)

Resto2 = D % 2
Resto3 = D % 3

if Resto2 == 0 and Resto3 == 0:
    print(D)