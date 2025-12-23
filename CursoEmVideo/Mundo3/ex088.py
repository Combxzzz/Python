from time import sleep
from random import randint

palpites = []

num_palpites = int(input("Quantos palpites quer gerar? "))

for i in range(num_palpites):
    palpite = []
    while len(palpite) < 6:
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpite.sort()
    palpites.append(palpite)

for i, p in enumerate(palpites):
    print(f"Palpite {i+1}: {p}")
    sleep(0.5)
