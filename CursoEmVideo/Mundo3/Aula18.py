# Aula18 - Listas (parte 2) - Listas dentro de listas

# -------------------------------------------------------------------
# Nesta aula aprendemos:
# - listas dentro de listas
# - cópia de listas
# - cuidado com ligações entre listas
# - percorrer estruturas compostas
# -------------------------------------------------------------------

# ---------------------------------------------------------
# LISTA COMPOSTA (LISTA DENTRO DE LISTA)
# ---------------------------------------------------------

# Cada elemento da lista principal é outra lista
pessoas = [["João", 25], ["Maria", 19], ["Pedro", 32]]

# Mostrando a lista completa
print(pessoas)

# Acessando dados internos
print(pessoas[0][0])  # nome da primeira pessoa
print(pessoas[1][1])  # idade da segunda pessoa

# ---------------------------------------------------------
# PROBLEMA COM CÓPIA DE LISTAS (ARMADILHA)
# ---------------------------------------------------------

teste = []
galera = []

# Adicionando dados na lista teste
teste.append("Lucas")
teste.append(20)

# Adicionando teste dentro de galera SEM cópia
galera.append(teste)

# Alterando teste
teste[0] = "Maria"
teste[1] = 30

print("\nGalera sem cópia:", galera)

# ---------------------------------------------------------
# JEITO CERTO — USANDO CÓPIA [:]
# ---------------------------------------------------------

teste = []
galera = []

# Primeiro cadastro
teste.append("Lucas")
teste.append(20)
galera.append(teste[:])  # cópia da lista

# Segundo cadastro
teste.clear()
teste.append("Ana")
teste.append(22)
galera.append(teste[:])  # nova cópia

print("Galera com cópia correta:", galera)

# ---------------------------------------------------------
# PERCORRENDO LISTAS COMPOSTAS
# ---------------------------------------------------------

print("\nPercorrendo a lista de pessoas:")
for pessoa in galera:
    print(f"Nome: {pessoa[0]} | Idade: {pessoa[1]}")

# ---------------------------------------------------------
# LISTA COMPOSTA COM INPUT DO USUÁRIO
# ---------------------------------------------------------

pessoas = []
dados = []

for c in range(0, 3):
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])  # salva a cópia
    dados.clear()             # limpa para próximo uso

print("\nDados cadastrados:")
for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos")

# ---------------------------------------------------------
# ANALISANDO DADOS DA LISTA COMPOSTA
# ---------------------------------------------------------

maiores = menores = 0

for p in pessoas:
    if p[1] >= 18:
        maiores += 1
    else:
        menores += 1

print(f"\nTotal de maiores de idade: {maiores}")
print(f"Total de menores de idade: {menores}")
