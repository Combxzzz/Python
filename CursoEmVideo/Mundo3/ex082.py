numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input("Digite um numero: ")))
    while True:
        opcao = str(input("Deseja continuar? [S/N] ")).upper()
        if opcao in "SN":
            break
        print("Digite um opcao valida")
    if opcao == "N":
        break

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f"numeros da lista: {numeros}.")
print(f"numeros pares na lista: {pares}.")
print(f"numeros impares na lista: {impares}.")