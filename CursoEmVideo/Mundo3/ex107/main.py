import moedas

p = float(input("Digite o preco: "))

print(f"A metade de {p}: {moedas.metade(p)}")
print(f"O dobro de {p}: {moedas.dobro(p)}")
print(f"Aumentando 10%, temos: {moedas.aumentar(p, 10)}")
print(f"Reduzindo 13%, temos: {moedas.diminuir(p, 13)}")