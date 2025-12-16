total_gasto = 0
mais_de_1000 = 0
mais_barato = ("", 0)
# Mesmo sendo um recurso mais avançado, usei coleções para deixar mais facil além de mais organizado
# Não sei se é o melhor jeito, mas foi o que pensei no momento

while True:
    produto = input("Nome do produto: ")
    preco = float(input("Preço: R$"))
    total_gasto += preco

    if preco > 1000:
        mais_de_1000 += 1

    if mais_barato is None or preco < mais_barato[1]:
        mais_barato = (produto, preco)

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N]: ").strip().upper()[0]

    if continuar == "N":
        break

print(f"O total gasto na compra foi R${total_gasto:.2f}")
print(f"Temos {mais_de_1000} produtos que custam mais de R$1000.00")
print(f"O produto mais barato foi {mais_barato[0]} que custa R${mais_barato[1]:.2f}")