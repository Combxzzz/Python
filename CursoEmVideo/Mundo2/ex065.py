contador = 0
soma = 0
menor = None
maior = None

while True:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1

    if menor is None or numero < menor:
        menor = numero

    if maior is None or numero > maior:
        maior = numero

    opcao = input("Quer continuar? [S/N]: ").strip().upper()
    while opcao not in ("S", "N"):
        print("Opção inválida!")
        opcao = input("Quer continuar? [S/N]: ").strip().upper()

    if opcao == "N":
        if contador < 2:
            print("Digite pelo menos 2 números.")
            continue
        break

media = soma / contador

print(f"Media dos numeros: {media}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
