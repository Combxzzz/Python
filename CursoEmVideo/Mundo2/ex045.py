import random

choiceUser = None
choiceMachi = None

opcoes = ["pedra" , "tesoura" , "papel"]

print("Escolha uma das opcoes abaixo\n")

user = int(input("""
1 - pedra
2 - tesoura
3 - papel\n
                 
escolha:
"""))

choiceMachi = random.choice(opcoes)
choiceUser = opcoes[user - 1]

print("\nescolha da maquina: {}\n".format(choiceMachi))
print("\nsua escolha: {}\n".format(choiceUser))

if choiceMachi == choiceUser:
    print("empate")
elif (
    (choiceUser == "pedra" and choiceMachi == "tesoura") or 
    (choiceUser == "tesoura" and choiceMachi == "papel") or 
    (choiceUser == "papel" and choiceMachi == "pedra")
):
    print("voce ganhou")
else:
    print("voce perdeu")