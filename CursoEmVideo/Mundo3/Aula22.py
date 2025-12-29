# Aula22 - Módulos e Pacotes em Python

# ---------------------------------------------------------
# Nessa aula aprendemos:
# - o que são módulos
# - como importar módulos
# - como criar módulos
# - o que são pacotes
# ---------------------------------------------------------

# ---------------------------------------------------------
# IMPORTANDO UM MÓDULO PRONTO DO PYTHON
# ---------------------------------------------------------

import math  # importa o módulo math inteiro

num = int(input("Digite um número: "))

# usando funções do módulo math
print(f"Raiz quadrada: {math.sqrt(num):.2f}")
print(f"Valor arredondado para cima: {math.ceil(num)}")
print(f"Valor arredondado para baixo: {math.floor(num)}")

# ---------------------------------------------------------
# IMPORTANDO APENAS FUNÇÕES ESPECÍFICAS
# ---------------------------------------------------------

from math import sqrt, ceil, floor

print(f"Raiz usando sqrt: {sqrt(num):.2f}")
print(f"Ceil: {ceil(num)}")
print(f"Floor: {floor(num)}")

# ---------------------------------------------------------
# CRIANDO UM MÓDULO (EXEMPLO)
# ---------------------------------------------------------
# Imagine que temos um arquivo chamado: uteis.py
#
# Conteúdo do arquivo uteis.py:
#
# def dobro(n):
#     return n * 2
#
# def triplo(n):
#     return n * 3
#
# def fatorial(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f
#
# ---------------------------------------------------------

# IMPORTANDO NOSSO MÓDULO CRIADO
# from uteis import dobro, triplo, fatorial
#
# print(dobro(5))
# print(triplo(5))
# print(fatorial(5))

# ---------------------------------------------------------
# O QUE SÃO PACOTES
# ---------------------------------------------------------
# Pacotes são pastas que organizam módulos
#
# Exemplo de estrutura:
#
# uteis/
# ├── __init__.py
# ├── numeros.py
# ├── textos.py
#
# ---------------------------------------------------------

# ---------------------------------------------------------
# EXEMPLO DE PACOTE
# ---------------------------------------------------------
# arquivo: uteis/numeros.py
#
# def dobro(n):
#     return n * 2
#
# def triplo(n):
#     return n * 3
#
# ---------------------------------------------------------
# arquivo: uteis/textos.py
#
# def maiuscula(txt):
#     return txt.upper()
#
# ---------------------------------------------------------

# USANDO FUNÇÕES DE UM PACOTE
# from uteis.numeros import dobro
# from uteis.textos import maiuscula
#
# print(dobro(10))
# print(maiuscula("python"))

# ---------------------------------------------------------
# BOAS PRÁTICAS
# ---------------------------------------------------------
# - módulos deixam o código organizado
# - facilitam manutenção
# - permitem reutilização de código
# - pacotes organizam projetos grandes
