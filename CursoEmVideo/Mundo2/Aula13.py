# Aula13 - Estruturas de Repetição For

# -------------------------------------------------------------------
# Na aula 13 aprendemos a repetir ações usando o comando FOR.
# O for percorre uma sequência de valores automaticamente.
# Estrutura:
# for i in range(inicio, fim, passo):
# -------------------------------------------------------------------

# Exemplo 1 — Contando de 0 até 5
print("Contando de 0 até 5:")
for c in range(0, 6):  # vai de 0 até 5 (o último número não entra)
    print(c)
print("FIM!")

# Exemplo 2 — Contando de 5 até 0 (ordem reversa)
print("Contando de 5 até 0:")
for c in range(5, -1, -1):  # começa em 5, vai até 0, passo -1
    print(c)
print("FIM!\n")

# Exemplo 3 — Pulando de 2 em 2
print("Contando de 0 até 10 pulando de 2:")
for c in range(0, 11, 2):  # de 2 em 2
    print(c)
print("FIM!\n")

# -------------------------------------------------------------------
# Exemplo 4 — Usando valores digitados pelo usuário
# -------------------------------------------------------------------
print("Contagem personalizada:")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

# OBS: se o passo for 0, o Python dá erro — por isso tratamos:
if passo == 0:
    passo = 1

for c in range(inicio, fim + 1, passo):
    print(c)
print("FIM!\n")

# -------------------------------------------------------------------
# Exemplo 5 — Somando valores dentro de um for
# -------------------------------------------------------------------
print("Somando números digitados:")

soma = 0  # acumulador
for c in range(1, 5):  # repete 4 vezes
    num = int(input(f"Digite o {c}º número: "))
    soma += num  # soma cada número no acumulador

print(f"A soma de todos os valores foi {soma}.\n")

# -------------------------------------------------------------------
# Exemplo 6 — Contando quantos itens foram digitados
# -------------------------------------------------------------------
print("Digite 5 números e eu conto quantos são pares:")

pares = 0
for c in range(1, 6):
    num = int(input(f"{c}º número: "))
    if num % 2 == 0:
        pares += 1

print(f"Você digitou {pares} números pares!\n")
