# Aula19 - Dicionários em Python

# -------------------------------------------------------------------
# Dicionários são estruturas de dados MUTÁVEIS.
# Eles funcionam com pares: CHAVE → VALOR.
# Diferente das listas, não usamos índices numéricos.
# São representados por chaves {}.
# -------------------------------------------------------------------

# Criando um dicionário
pessoa = {
    "nome": "Lucas",
    "idade": 25,
    "sexo": "M"
}

# Mostrando o dicionário completo
print(pessoa)

# ---------------------------------------------------------
# ACESSANDO VALORES DO DICIONÁRIO
# ---------------------------------------------------------

# Acessando valores pelas chaves
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["sexo"])

# ---------------------------------------------------------
# ADICIONANDO E ALTERANDO DADOS
# ---------------------------------------------------------

# Adicionando uma nova chave
pessoa["peso"] = 70.5

# Alterando um valor existente
pessoa["idade"] = 26

print(pessoa)

# ---------------------------------------------------------
# REMOVENDO DADOS
# ---------------------------------------------------------

# del remove uma chave do dicionário
del pessoa["sexo"]

print(pessoa)

# ---------------------------------------------------------
# PERCORRENDO DICIONÁRIOS
# ---------------------------------------------------------

print("\nPercorrendo o dicionário:")

# Percorrendo as chaves
for chave in pessoa.keys():
    print(chave)

# Percorrendo os valores
for valor in pessoa.values():
    print(valor)

# Percorrendo chave e valor juntos
for chave, valor in pessoa.items():
    print(f"{chave} = {valor}")

# ---------------------------------------------------------
# DICIONÁRIOS DENTRO DE LISTAS
# ---------------------------------------------------------

brasil = []
estado1 = {"uf": "São Paulo", "sigla": "SP"}
estado2 = {"uf": "Rio de Janeiro", "sigla": "RJ"}

# Adicionando dicionários na lista
brasil.append(estado1)
brasil.append(estado2)

print("\nLista com dicionários:", brasil)

# Percorrendo lista de dicionários
for estado in brasil:
    print(f"{estado['uf']} - {estado['sigla']}")

# ---------------------------------------------------------
# CADASTRO COM DICIONÁRIOS (INPUT)
# ---------------------------------------------------------

cadastro = {}
pessoas = []

for c in range(0, 2):
    cadastro["nome"] = input("Nome: ")
    cadastro["idade"] = int(input("Idade: "))
    cadastro["sexo"] = input("Sexo [M/F]: ").strip().upper()

    pessoas.append(cadastro.copy())  # copia o dicionário
    cadastro.clear()                 # limpa para o próximo

print("\nPessoas cadastradas:")
for p in pessoas:
    print(f"{p['nome']} - {p['idade']} anos - {p['sexo']}")
