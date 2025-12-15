soma = 0
numeros_digitados = 0
while True:
    numero = int(input("Digite um numero (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    numeros_digitados += 1


print(f"Voce digitou {numeros_digitados} numeros e a soma entre eles foi {soma}.")