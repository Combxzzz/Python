pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(input("Digite o nome da pessoa: "))
    dados.append(float(input("Digite o peso da pessoa: ")))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opcao = input("Deseja continuar? [S/N] ").upper()
    while opcao not in "SN":
        opcao = input("Deseja continuar? [S/N] ").upper()
    if opcao == 'N':
        break

print(f"Foram cadastradas {len(pessoas)} pessoas")

print(f"O maior peso foi {maior}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")

print(f"\nO menor peso foi {menor}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
