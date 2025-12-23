from random import randint
from time import sleep

resultados = dict()

resultados['jogador1'] = randint(1, 6)
resultados['jogador2'] = randint(1, 6)
resultados['jogador3'] = randint(1, 6)
resultados['jogador4'] = randint(1, 6)

print(resultados)
print("Valores sorteados:")
for k, v in resultados.items():
    print(f"    O {k} tirou {v}")
    sleep(0.5)

dicionario_sorted = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

print(dicionario_sorted)

print("RANKING DOS JOGADORES: ")
for i, (k, v) in enumerate(dicionario_sorted.items()):
    print(f"    {i + 1}º {k}: {v}")
    sleep(0.5)
