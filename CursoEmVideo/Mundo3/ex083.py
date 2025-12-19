expressao = str(input("Digite um expressao: "))

pilhas = []

for simbolo in expressao:
    if simbolo == "(":
        pilhas.append(simbolo)
    elif simbolo == ")":
        if len(pilhas) > 0:
            pilhas.pop()
        else:
            pilhas.append(")")
            break

if len(pilhas) == 0:
    print("Expressao correta")
else:
    print("Expressao incorreta")
