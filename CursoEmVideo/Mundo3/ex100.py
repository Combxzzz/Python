import random

def sortear(lista):
    for i in range(5):
        lista.append(random.randint(1, 10))


def somar_par(args):
    soma = 0
    pares = []
    for i in args:
        if i % 2 == 0:
            soma += i
            pares.append(i)
    print(f"A soma dos numeros: {pares} foi de {soma}")


numeros = []
sortear(numeros)

print(f"numeros sorteados: {numeros}")
somar_par(numeros)