valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
valorC = int(input("Digite o valor de C: "))

if valorA < valorB and valorA < valorC:
    print("O menor valor é A:", valorA)
elif valorB < valorA and valorB < valorC:
    print("O menor valor é B:", valorB)
else:
    print("O menor valor é C:", valorC)