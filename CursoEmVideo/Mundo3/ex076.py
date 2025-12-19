produtos_precos = (
    "Lapis", 1.75,
    "Borracha", 2.00,
    "Caderno", 15.90,
    "Estojo", 25.00,
    "Transferidor", 4.20,
    "Compasso", 9.99,
    "Mochila", 120.32,
    "Caneta", 22.30,
    "Livro", 34.90
)

for i in range(0, len(produtos_precos), 2):
    produto = produtos_precos[i]
    preco = produtos_precos[i + 1]
    print(f"{produto:<15} R$ {preco:>6.2f}")
    