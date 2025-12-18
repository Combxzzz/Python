numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete" ,"oito", "nove", "dez")
while True:
    user = int(input("Digite um numero (0 a 10): "))
    if user < 0 or user > 10:
        print("tente novamente")
        continue
    else:
        print(f"Voce digitou o numero {numeros[user]}")
        continuar = input("Deseja continuar? [S/N] ").upper()
        if continuar in "N":
            break
        elif continuar in "S":
            continue
        else:
            print("Digite uma opção valida")
