import random

machi = random.randint(0, 10)
tentativas = 0
print("A maquina pensou em um numero entre 0 e 10, tente adivinhar.")
user = int(input("Digite seu palpite: "))
acerto = False

# while True:
#     user = int(input("Escolha um numero entre 0 a 10: "))
#     if user == machi
#         print("voce acertou!")
#         break
#     else:
#         print("Voce errou, tente novamente")
#         tentativas += 1

# print(f"Palpites: {tentativas}")
# print(f"Máquina: {machi} | Você: {user}")

while user != machi:
    print("Voce errou!")
    tentativas += 1
    if user > machi:
        print("numero da maquina é menor")
    elif user < machi:
        print("numero da maquina é maior.")
    user = int(input("Digite seu palpite: "))

print(f"Voce acertou na {tentativas + 1} tentativas")
print(f"a maquina escolheu o numero {machi}.")

# while not acerto:
#     user = int(input("Digite seu palpite: "))
#     tentativas += 1
#     if user == machi:
#         acerto = True
#     else:
#         if user < machi:
#             print("Maior...")
#         elif user > machi:
#             print("Menor...")

# print(f"Voce deu {tentativas} palpites.")
# print(f"a maquina escolheu {machi}")