dias = int(input("Dias alugados: "))
km = float(input("Km rodados: "))
preco = (dias * 60) + (km * 0.15)
print(f"O total a pagar é R$ {preco:.2f}")