from random import randint
print("Par ou impar")
print("--" * 15)
vitorias = 0

while True:

    user = int(input("Digite um numero para jogar: "))
    escolha = str(input("Par ou impar? [P/I]: ")).strip().upper()[0]

    while escolha not in "PI":
        print("Escolha invalida, tente novamente.")
        escolha = str(input("Par ou impar? [P/I]: ")).strip().upper()[0]

    computador = randint(0, 10)
    total = user + computador

    print(f"Voce jogou {user} e o computador {computador}. Total de {total} ", end="")

    if total % 2 == 0:
        print("Deu PAR")
        if escolha == "P":
            print("Voce VENCEU!")
            vitorias += 1
        else:
            print("Voce PERDEU!")
            break

    else:
        print("Deu IMPAR")
        if escolha == "I":
            print("Voce VENCEU!")
            vitorias += 1
        else:
            print("Voce PERDEU!")
            break

    print("Vamos jogar novamente...")

print(f"Acabou, sua Win-Streak foi de {vitorias}.")