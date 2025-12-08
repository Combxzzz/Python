Ndig = 0
Soma = 0

while True:
    N1 = int(input("Digite um numero: "))
    if N1 == 999:
        break
    Ndig += 1
    Soma += N1

print(f"Numeros digitados: {Ndig}")
print(f"A soma é: {Soma}")