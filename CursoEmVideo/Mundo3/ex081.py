numeros = []

while True:
    numeros.append(int(input("Digite um número: ")))

    while True:
        opcao = input("Deseja continuar? [S/N] ").upper()
        if opcao in "SN":
            break
        print("Digite uma opção válida!")

    if opcao == "N":
        break

print(numeros)
print(f"Foram digitados {len(numeros)} números")
print(f"Lista em ordem decrescente: {sorted(numeros, reverse=True)}")

if 5 in numeros:
    print(f"O número 5 aparece {numeros.count(5)} vez(es)")
else:
    print("O número 5 não está na lista")
