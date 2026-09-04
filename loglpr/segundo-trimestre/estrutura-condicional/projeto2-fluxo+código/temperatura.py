escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

temperatura = float(input("Digite a temperatura: "))

if escala == "F":
    celsius = 5 / 9 * (temperatura - 32)
    print(f"Temperatura equivalente em Celsius: {celsius:.2f}")

elif escala == "C":
    fahrenheit = temperatura * 9 / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")