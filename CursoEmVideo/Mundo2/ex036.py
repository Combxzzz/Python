casa = float(input("Qual o valor da casa: "))
salario = float(input("Quanto voce recebe: "))
tempo = int(input("Em quanto tempo voce quer pagar (em meses): "))

prest = casa / tempo

limite = salario * 0.3

if prest > limite:
    print("tu nao pode comprar essa casa")
else:
    print("tu pode comprar essa casa")