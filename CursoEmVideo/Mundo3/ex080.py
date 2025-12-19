lista = []

for i in range(5):
    numero = int(input("Digite um número: "))

    if not lista:
        lista.append(numero)
        print("Adicionado no final da lista")
    else:
        for pos, num in enumerate(lista):
            if numero < num:
                print(f"Inserindo na posicão {pos}")
                lista.insert(pos, numero)
                break
        else:
            lista.append(numero)
            print(f"Adicionado no final da lista")

print(lista)
