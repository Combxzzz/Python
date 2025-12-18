from random import randint

numeros = []
for i in range(0, 6):
    numeros.append(randint(1, 100))
numeros = tuple(numeros)

print(numeros)
print(f"Maior valor na tupla: {max(numeros)}")
print(f"Menor valor na tupla: {min(numeros)}")