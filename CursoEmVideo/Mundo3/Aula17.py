# Aula17 - Listas em Python

# -------------------------------------------------------------------
# Listas são estruturas de dados MUTÁVEIS.
# Diferente das tuplas, podemos alterar, adicionar e remover elementos.
# São representadas por colchetes [].
# -------------------------------------------------------------------

# Criando uma lista
lanche = ["Hambúrguer", "Suco", "Pizza", "Pudim"]

# Mostrando a lista completa
print(lanche)

# ---------------------------------------------------------
# ACESSANDO ELEMENTOS DA LISTA
# ---------------------------------------------------------

# Acessando elementos pelo índice
print(lanche[0])      # primeiro elemento
print(lanche[2])      # terceiro elemento

# Acessando do fim para o início
print(lanche[-1])     # último elemento

# Fatiamento da lista
print(lanche[1:3])    # do índice 1 ao 2

# ---------------------------------------------------------
# ALTERANDO ELEMENTOS DA LISTA
# ---------------------------------------------------------

# Alterando um valor da lista
lanche[3] = "Sorvete"
print(lanche)

# ---------------------------------------------------------
# ADICIONANDO ELEMENTOS NA LISTA
# ---------------------------------------------------------

# append() adiciona no FINAL da lista
lanche.append("Cookie")
print(lanche)

# insert() adiciona em uma posição específica
lanche.insert(1, "Cachorro-quente")
print(lanche)

# ---------------------------------------------------------
# REMOVENDO ELEMENTOS DA LISTA
# ---------------------------------------------------------

# del remove pelo índice
del lanche[0]
print(lanche)

# pop() remove pelo índice (ou o último se não passar índice)
lanche.pop()
print(lanche)

# remove() remove pelo valor
lanche.remove("Pizza")
print(lanche)

# ---------------------------------------------------------
# ORGANIZANDO LISTAS
# ---------------------------------------------------------

valores = [8, 2, 5, 4, 9, 3]
print("\nLista de valores:", valores)

# sort() organiza a lista
valores.sort()
print("Valores em ordem crescente:", valores)

# sort(reverse=True) organiza em ordem decrescente
valores.sort(reverse=True)
print("Valores em ordem decrescente:", valores)

# ---------------------------------------------------------
# FUNÇÕES ÚTEIS COM LISTAS
# ---------------------------------------------------------

print(f"\nQuantidade de elementos: {len(valores)}")
print(f"Maior valor: {max(valores)}")
print(f"Menor valor: {min(valores)}")
print(f"Soma dos valores: {sum(valores)}")

# ---------------------------------------------------------
# PERCORRENDO LISTAS COM FOR
# ---------------------------------------------------------

print("\nPercorrendo a lista com FOR:")
for item in lanche:
    print(item)

# Percorrendo com enumerate
print("\nPercorrendo com enumerate:")
for pos, item in enumerate(lanche):
    print(f"Na posição {pos} está {item}")

# ---------------------------------------------------------
# CRIANDO LISTAS A PARTIR DE INPUT
# ---------------------------------------------------------

numeros = []

for c in range(0, 5):
    numeros.append(int(input("Digite um número: ")))

print("Números digitados:", numeros)