import random

opcoes = ["pedra" , "tesoura" , "papel"]

print("Suas opcoes: \n[ 1 ] pedra\n[ 2 ] tesoura\n[ 3 ] papel")
user = int(input("Qual e a sua escolha? \nEscolha: "))

choiceMachi = random.choice(opcoes)
choiceUser = opcoes[user - 1]

print("escolha da maquina: {}".format(choiceMachi))
print("sua escolha: {}".format(choiceUser))

if choiceMachi == choiceUser:
    print("Resultado: Empate")
elif (
    (choiceUser == "pedra" and choiceMachi == "tesoura") or 
    (choiceUser == "tesoura" and choiceMachi == "papel") or 
    (choiceUser == "papel" and choiceMachi == "pedra")
):
    print(f"Voce venceu, {choiceUser} vence {choiceMachi}")
else:
    print(f"Voce perdeu, {choiceMachi} vence {choiceUser}")