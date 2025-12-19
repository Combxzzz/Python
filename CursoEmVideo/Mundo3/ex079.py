numeros = []

while True:
    num = int(input("Digite um numero: "))
    if num in numeros:
        print("Numero existe")
        print("Nao adicionado...")
        continue
    else:
        numeros.append(num)
        option = input("Deseja adicionar? [S/N]").upper()
        if option == "S":
            continue
        elif option == "N":
            break
        else:
            print("Opção invalida, digite novamente...")
            option = input("Deseja adicionar? [S/N]").upper()

print(sorted(numeros))