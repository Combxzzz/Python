numeros = []
for i in range(0, 5):
    numeros.append(int(input(f"Digite o {i} numero: ")))

maior = max(numeros)
menor = min(numeros)

print(f"o numero {maior} apareceu nas posicões: ", end="")
for p, n in enumerate(numeros):
    if n == maior:
        print(f"{p}", end="...")
print()

print(f"O menor numero {menor} apareceu nas posicções: ", end="")
for p, n in enumerate(numeros):
    if n == menor:
        print(f"{p}", end="...")
