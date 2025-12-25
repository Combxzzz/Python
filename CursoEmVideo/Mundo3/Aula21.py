# Aula21 - Funções em Python (parte 2)

# -------------------------------------------------------------------
# Nesta aula aprendemos:
# - funções com retorno (return)
# - docstrings (documentação de funções)
# - parâmetros opcionais
# - escopo de variáveis
# -------------------------------------------------------------------

# ---------------------------------------------------------
# FUNÇÃO COM RETORNO
# ---------------------------------------------------------

def soma(a, b):
    # retorna a soma de dois valores
    return a + b

# usando o retorno da função
resultado = soma(3, 7)
print(f"Soma: {resultado}")

# ---------------------------------------------------------
# DOCSTRING (DOCUMENTAÇÃO DA FUNÇÃO)
# ---------------------------------------------------------

def contador(inicio, fim, passo):
    """
    → Faz uma contagem e mostra na tela.
    :param inicio: valor inicial da contagem
    :param fim: valor final da contagem
    :param passo: passo da contagem
    :return: sem retorno
    """
    for c in range(inicio, fim + 1, passo):
        print(c, end=" ")
    print()

# ajuda da função (mostra a docstring)
help(contador)

# ---------------------------------------------------------
# PARÂMETROS OPCIONAIS
# ---------------------------------------------------------

def somar(a=0, b=0, c=0):
    # se não passar algum valor, ele vale 0
    return a + b + c

print(somar(2, 3))
print(somar(2, 3, 4))
print(somar())

# ---------------------------------------------------------
# ESCOPO DE VARIÁVEIS
# ---------------------------------------------------------

def teste():
    # variável local (só existe dentro da função)
    x = 8
    print(f"Valor de x dentro da função: {x}")

# variável global
x = 5

teste()
print(f"Valor de x fora da função: {x}")

# ---------------------------------------------------------
# USANDO 'global' (não recomendado)
# ---------------------------------------------------------

def alterar():
    global x
    x = 10

alterar()
print(f"Novo valor de x global: {x}")

# ---------------------------------------------------------
# FUNÇÃO RETORNANDO MAIS DE UM VALOR
# ---------------------------------------------------------

def maior_menor(lista):
    # retorna o maior e o menor valor de uma lista
    return max(lista), min(lista)

valores = [2, 4, 6, 1, 9]
maior, menor = maior_menor(valores)

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
