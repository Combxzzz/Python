import moedas


p = float(input("Digite o preco: "))

print(f"A metade de {moedas.converter(p)}: {moedas.metade(p, converte=True)}")
print(f"O dobro de {moedas.converter(p)}: {moedas.dobro(p, converte=True)}")
print(f"Aumentando 10%, temos: {moedas.aumentar(p, 10, converte=True)}")
print(f"Reduzindo 13%, temos: {moedas.diminuir(p, 13, converte=True)}")