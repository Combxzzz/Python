soma = 0
numeros_digitados = 0

while True:
    numero = int(input("Digite outro numero para somar(999 para parar): "))
    if numero == 999:
        break
    numeros_digitados += 1
    soma += numero

print(f"A soma dos valores foi {soma} e foram digitados {numeros_digitados} números.")