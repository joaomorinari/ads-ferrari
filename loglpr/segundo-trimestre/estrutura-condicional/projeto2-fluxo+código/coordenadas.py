x = float(input("digite a posicao X: "))
y = float(input("digite a posicao Y: "))

if x == 0 and y == 0:
    position = "Origem"

elif x == 0:
    position = "Eixo Y"

elif y == 0:
    position = "Eixo X"

elif x > 0 and y > 0:
    position = "Q1"

elif x < 0 and y > 0:
    position = "Q2"

elif x < 0 and y < 0:
    position = "Q3"

elif x > 0 and y < 0:
    position = "Q4"

print(position)