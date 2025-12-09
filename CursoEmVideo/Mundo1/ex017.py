from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")