#Aula8 - Utilizando Modulos em Python
import math

# nesse caso importamos a biblioteca math para usar funções matemáticas
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz quadrada de {num} é igual a {raiz:.2f}")
print(f"O valor arredondado para cima é {math.ceil(raiz)}")
print(f"O valor arredondado para baixo é {math.floor(raiz)}")

# existem varias outras funções na biblioteca math, como por exemplo:

# math.factorial(x) - calcula o fatorial de x
# math.pow(x, y) - calcula x elevado a y
# math.sin(x), math.cos(x), math.tan(x) - funções trigonométricas

# também podemos importar apenas partes específicas de uma biblioteca, ex:
# from math import sqrt, ceil, floor
# isso importa apenas as funções sqrt, ceil e floor da biblioteca math


# também existe a biblioteca random para gerar números aleatórios
import random
num_aleatorio = random.randint(1, 100) # gera um número aleatório entre 1 e 100
print(f"Número aleatório gerado: {num_aleatorio}") # imprime o número gerado

# outras funções da biblioteca random incluem:
# random.random() - gera um número float aleatório entre 0.0 e 1.0
# random.choice(seq) - escolhe um elemento aleatório de uma sequência (lista, tupla, etc)
# random.shuffle(seq) - embaralha os elementos de uma sequência


# Por fim, a biblioteca datetime para trabalhar com datas e horas
from datetime import datetime
agora = datetime.now() # obtém a data e hora atual
print(f"Data e hora atual: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# outras funções da biblioteca datetime incluem:
# datetime.date(year, month, day) - cria uma data específica
# datetime.time(hour, minute, second) - cria um horário específico
# datetime.timedelta - representa uma duração, a diferença entre duas datas ou horas

# Essas são apenas algumas das muitas bibliotecas disponíveis em Python para facilitar o desenvolvimento de programas, existem muitas outras para diversas finalidades.