n1 = int(input("digite o primeiro número: "))
n2 = int(input("digite o segundo número: "))

if n1 > n2:
    print(f"O valor {n1} é maior que {n2}")
elif n2 > n1:
    print(f"O valor {n2} é maior que {n1}")
else:
    print("Os dois valores são iguais")