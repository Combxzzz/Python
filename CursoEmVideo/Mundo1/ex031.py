dist = float(input("Qual a distância da viagem em km? "))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f"O preço da passagem é R$ {preco:.2f}")