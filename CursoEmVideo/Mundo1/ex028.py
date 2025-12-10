from random import randint
from time import sleep

computador = randint(0, 5)
print("--" * 30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("--" * 30)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)
if jogador == computador:
    print(f"PARABÉNS! Você me venceu! Eu tinha escolhido o número {computador}.")
else:
    print(f"GANHEI! Eu pensei no número {computador} e não no {jogador}!")
