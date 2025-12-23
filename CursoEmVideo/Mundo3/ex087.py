matriz = [[], [], []]
soma_pares = 0

for i in range(0, 3):
    matriz[0].append(int(input(f"Digite o valor da posicao [0, {i}]: ")))
for i in range(0, 3):
    matriz[1].append(int(input(f"Digite o valor da posicao [1, {i}]: ")))
for i in range(0, 3):
    matriz[2].append(int(input(f"Digite o valor da posicao [2, {i}]: ")))


for index, num in enumerate(matriz[0]):
    if num % 2 == 0:
        soma_pares += num
for index, num in enumerate(matriz[1]):
    if num % 2 == 0:
        soma_pares += num
for index, num in enumerate(matriz[2]):
    if num % 2 == 0:
        soma_pares += num


print(matriz[0])
print(matriz[1])
print(matriz[2])

print("-" * 20)

print(f"Soma dos numeros pares digitados: {soma_pares}")
print(f"Soma dos valores da terceira coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}")
print(f"Maior valor da segunda coluna: {max(matriz[1])}")
