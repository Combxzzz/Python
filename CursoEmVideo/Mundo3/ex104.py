def leia_int(msg):
    numero = input(msg)

    while not numero.isnumeric():
        print("ERRO: Digite um número inteiro.")
        numero = input(msg)

    return int(numero)

n = leia_int("Digite um numero: ")

print(f'O numero digitado foi {n}')