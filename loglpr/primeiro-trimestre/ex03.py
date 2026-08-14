nome1 = input("Dados da primeira pessoa:\nNome: ")
idade1 = int(input("Idade: "))

nome2 = input("Dados da segunda pessoa:\nNome: ")
idade2 = int(input("Idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome1} e {nome2} eh de {media:.1f} anos")