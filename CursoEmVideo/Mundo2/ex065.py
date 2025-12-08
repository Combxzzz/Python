Ndig = 0
soma = 0
Me = None
Ma = None

while True:
    n1 = float(input("Digite um numero: "))
    Ndig += 1
    soma += n1

    if Me is None:
        Me = n1
    else:
        if n1 <= Me:
            Me = n1

    if Ma is None:
        Ma = n1
    else:
        if n1 >= Ma:
            Ma = n1

    op = input("Quer continuar? [S/N]: ").upper()
    while op not in ["S","N"]:
        print("Opçao invalida!")
        op = input("Quer continuar? [S/N]: ").upper()

    if op == "N" and Ndig < 2:
        print("Digite mais de 2 numeros...")
        Ndig = 0
        Me = None
        Ma = None
        continue

    if op == "N":
        break


print(f"A media de todos os numeros é {soma/Ndig}")
print(f"Menor: {Me}")
print(f"Maior: {Ma}")