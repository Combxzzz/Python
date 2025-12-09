lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")

print(lanche[0]) #Pega o primeiro elemento
print(lanche[-2]) #Pega o penultimo elemento
print(lanche[1:3]) #Desconsidera o ultimo elemento
print(lanche[2:]) #Elemento 2 ate o final
print(lanche[:2]) #Pega do primeiro elemento ate o elemento 1
print(lanche[-3:]) #Começa no suco e vai até o final
print(len(lanche)) #Mostra o numero de itens
print(sorted(lanche)) #Mostra a lista organizada

print("-"*20)

for c in lanche:
    print(c)
    #exibe cada item na tupla

print("-"*20)

for cont in range(0, len(lanche)):
    print(lanche[cont])

print("-"*20)

for pos, comida in enumerate(lanche):
    print(f"posição {pos}, comida {comida}")
    # Exibe o index e o nome do elemento