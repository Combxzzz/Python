import random

def sortear(lista):
    for i in range(5):
        lista.append(random.randint(1, 10))


def somar_par(args, alvo):
    soma = 0
    for i in args:
        if i % 2 == 0:
            soma += i
    alvo.append(soma)


numeros = []
sortear(numeros)

pares = []
somar_par(numeros, pares)

print(numeros)
print(pares)