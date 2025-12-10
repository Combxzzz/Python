#Aula6 - Tipos Primitivos e Saída de Dados

n1 = input("Digite um valor: ") # guarda o valor numa variável
n2 = input("Digite outro valor: ") # o output sempre é uma string
s = n1 + n2 # soma as duas strings
print('A soma vale', s) # concatena as duas strings ou seja, junta as duas não soma

# para somar dois números, precisamos converter as strings para inteiros ou reais

# existem 4 tipos primitivos em Python:

# int - números inteiros, positivos ou negativos, sem casas decimais. Ex: 7, -4, 0, 9875
# float - números reais, com casas decimais. Ex: 4.5, 0.076, -15.223, 7.0
# bool - valores lógicos (verdadeiro ou falso). Ex: True, False
# str - cadeia de caracteres, textos. Ex: 'Olá', "1234", 'True'

n1 = int(input("Digite um valor: ")) # converte a string para inteiro
n2 = int(input("Digite outro valor: ")) # converte a string para inteiro
s = n1 + n2 # soma os dois números
print('A soma vale', s) # agora sim, soma os dois números