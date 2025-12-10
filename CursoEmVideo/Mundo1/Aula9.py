# Aula9 - Manipulação de Strings em Python

# Aqui estamos definindo uma string fixa
frase = "Curso em Vídeo Python"

# imprime a frase inteira
print(frase)

# ---------------------------------------------------------
# FATIAMENTO DE STRINGS
# ---------------------------------------------------------

# imprime os caracteres da posição 9 até a 13 (14 não entra)
print(frase[9:14])

# imprime os primeiros 5 caracteres (do início até o índice 5)
print(frase[:5])

# imprime do índice 15 até o final da string
print(frase[15:])

# imprime do índice 9 até o final, pulando de 3 em 3
print(frase[9::3])

# ---------------------------------------------------------
# ANÁLISE DE STRINGS
# ---------------------------------------------------------

# len() retorna o tamanho total da string (quantos caracteres ela tem)
print(len(frase))

# count() conta quantas vezes o caractere informado aparece
print(frase.count('o'))

# find() retorna a posição onde a palavra começa
# se não encontrar, retorna -1
print(frase.find('Vídeo'))

# ---------------------------------------------------------
# TRANSFORMAÇÕES DE STRINGS
# ---------------------------------------------------------

# replace() troca uma palavra por outra (não altera a original)
print(frase.replace('Python', 'Android'))

# upper() transforma tudo em MAIÚSCULAS
print(frase.upper())

# lower() transforma tudo em minúsculas
print(frase.lower())

# capitalize() deixa só a primeira letra maiúscula + resto minúsculo
print(frase.capitalize())

# title() deixa TODAS as palavras com a primeira letra maiúscula
print(frase.title())

# strip() remove espaços no início e no fim da string
# (aqui não tem espaços, mas serve de exemplo)
print(frase.strip())

# ---------------------------------------------------------
# DIVISÃO E JUNÇÃO DE STRINGS
# ---------------------------------------------------------

# split() divide a frase em uma lista, separando por espaços
print(frase.split())

# join() junta cada caractere da frase usando '-' entre eles
# (atenção: ele junta **caractere por caractere**, não palavras)
print('-'.join(frase))
