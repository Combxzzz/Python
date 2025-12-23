matriz = [[], [], []]

for i in range(0, 3):
    matriz[0].append(int(input(f"Digite o valor da posicao [0, {i}]: ")))
for i in range(0, 3):
    matriz[1].append(int(input(f"Digite o valor da posicao [1, {i}]: ")))
for i in range(0, 3):
    matriz[2].append(int(input(f"Digite o valor da posicao [2, {i}]: ")))

print(matriz[0])
print(matriz[1])
print(matriz[2])