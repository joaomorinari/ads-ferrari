inicio = int(input("Hora inicial: "))
final = int(input("Hora final: "))

if inicio == final:
    duracao = 24
elif final > inicio:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final

print("O JOGO DUROU", duracao, "HORA(S)")