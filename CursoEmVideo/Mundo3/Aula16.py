# Aula16 - Tuplas em Python

# -------------------------------------------------------------------
# Tuplas são estruturas de dados IMUTÁVEIS.
# Isso significa que, depois de criadas, NÃO podem ser alteradas.
# São representadas por parênteses ().
# -------------------------------------------------------------------

# Criando uma tupla simples
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")

# Mostrando a tupla completa
print(lanche)

# ---------------------------------------------------------
# ACESSANDO ELEMENTOS DA TUPLA
# ---------------------------------------------------------

# Acessando elementos pelo índice
print(lanche[0])    # primeiro elemento
print(lanche[2])    # terceiro elemento

# Acessando do fim para o início
print(lanche[-1])   # último elemento

# Fatiamento da tupla (funciona igual string)
print(lanche[1:3])  # do índice 1 ao 2

# ---------------------------------------------------------
# PERCORRENDO TUPLAS COM FOR
# ---------------------------------------------------------

print("\nPercorrendo a tupla:")
for comida in lanche:
    print(f"Eu vou comer {comida}")

# Percorrendo usando índices
print("\nPercorrendo com índices:")
for pos in range(0, len(lanche)):
    print(f"Na posição {pos} temos {lanche[pos]}")

# Percorrendo usando enumerate
print("\nUsando enumerate:")
for pos, comida in enumerate(lanche):
    print(f"Na posição {pos} está {comida}")

# ---------------------------------------------------------
# FUNÇÕES ÚTEIS COM TUPLAS
# ---------------------------------------------------------

# len() — tamanho da tupla
print(f"\nA tupla tem {len(lanche)} elementos.")

# count() — conta quantas vezes um item aparece
print(f"'Pizza' aparece {lanche.count('Pizza')} vez(es).")

# index() — mostra a posição da primeira ocorrência
print(f"'Suco' está na posição {lanche.index('Suco')}.")

# ---------------------------------------------------------
# TUPLAS COM NÚMEROS
# ---------------------------------------------------------

numeros = (4, 2, 9, 1, 5, 2)

print("\nTupla de números:", numeros)

# maior e menor valor
print(f"Maior valor: {max(numeros)}")
print(f"Menor valor: {min(numeros)}")

# soma dos valores
print(f"Soma dos valores: {sum(numeros)}")

# ---------------------------------------------------------
# TUPLAS SÃO IMUTÁVEIS
# ---------------------------------------------------------
