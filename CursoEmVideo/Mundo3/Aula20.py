# Aula20 - Funções em Python (parte 1)

# -------------------------------------------------------------------
# Funções servem para organizar o código, evitar repetição
# e facilitar a leitura.
#
# Estrutura básica de uma função:
# def nome_da_funcao():
#     comandos
# -------------------------------------------------------------------

# ---------------------------------------------------------
# FUNÇÃO SIMPLES (SEM PARÂMETROS)
# ---------------------------------------------------------

def linha():
    # essa função apenas imprime uma linha decorativa
    print("-" * 30)

# chamando a função
linha()
print("     SISTEMA PRINCIPAL")
linha()

# ---------------------------------------------------------
# FUNÇÃO COM PARÂMETROS
# ---------------------------------------------------------

def mensagem(texto):
    # recebe um texto e imprime formatado
    print("-" * 30)
    print(texto)
    print("-" * 30)

# chamando a função com argumentos
mensagem("Bem-vindo ao Curso de Python!")
mensagem("Aula 20 - Funções")

# ---------------------------------------------------------
# FUNÇÃO COM MAIS DE UM PARÂMETRO
# ---------------------------------------------------------

def soma(a, b):
    # soma dois números recebidos
    resultado = a + b
    print(f"A soma entre {a} e {b} é {resultado}")

# chamando a função
soma(3, 5)
soma(10, 20)

# ---------------------------------------------------------
# FUNÇÃO COM LAÇO INTERNO
# ---------------------------------------------------------

def contador(inicio, fim, passo):
    # faz uma contagem personalizada
    for c in range(inicio, fim + 1, passo):
        print(c, end=" ")
    print()

# chamando a função
contador(1, 10, 1)
contador(0, 10, 2)

# ---------------------------------------------------------
# FUNÇÃO COM LISTA COMO PARÂMETRO
# ---------------------------------------------------------

def dobra(lista):
    # dobra os valores de uma lista
    for i in range(len(lista)):
        lista[i] *= 2

valores = [1, 2, 3, 4, 5]
print("Lista original:", valores)

dobra(valores)
print("Lista dobrada:", valores)

# ---------------------------------------------------------
# FUNÇÃO COM RETORNO (introdução)
# ---------------------------------------------------------

def multiplicar(a, b):
    # retorna o resultado da multiplicação
    return a * b

resultado = multiplicar(4, 5)
print(f"Resultado da multiplicação: {resultado}")
