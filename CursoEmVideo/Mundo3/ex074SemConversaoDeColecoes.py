from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), )

print(numeros)
print(f"Maior numero na tupla: {max(numeros)}")
print(f"Menor numero na tupla: {min(numeros)}")