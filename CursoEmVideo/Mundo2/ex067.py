while True:
    numero = int(input("Digite um numero para ver sua tabuada (digite um numero negativo para parar): "))
    if numero < 0:
        print("programa tabuada encerrado")
        break
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
