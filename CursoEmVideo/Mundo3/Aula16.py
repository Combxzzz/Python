lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")

#indices       0          1        2        3
#indices      -4         -3       -2       -1

# tuplas são imutaveis
# lanche[1] = "Refrigerante" # Isso gera um erro
# lanche.append("Refrigerante") # Isso gera um erro
print(lanche[0]) #Pega o primeiro elemento
print(lanche[-2]) #Pega o penultimo elemento
print(lanche[1:3]) #Desconsidera o ultimo elemento
print(lanche[2:]) #Elemento 2 ate o final
print(lanche[:2]) #Pega do primeiro elemento ate o elemento 1
print(lanche[-3:]) #Começa no suco e vai até o final
print(len(lanche)) #Mostra o numero de itens
print(sorted(lanche)) #Mostra a lista organizada

# metodos para tuplas são limitados
# lanche.count("Pizza") #Conta quantas vezes o elemento aparece na tupla
# lanche.index("Pudim") #Mostra a posição do elemento na tupla
# esses são os unicos metodos para tuplas

print("-"*20)

# podemos percorrer uma tupla com o for

for c in lanche:
    print(c)
    #exibe cada item na tupla

print("-"*20)

for cont in range(0, len(lanche)):
    print(lanche[cont])
    # exibe cada item na tupla usando o indice como referencia

print("-"*20)

for pos, comida in enumerate(lanche):
    print(f"posição {pos}, comida {comida}")
    # Exibe o index e o valor da tupla