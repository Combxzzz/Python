peso_pessoas = []

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa (kg): "))
    peso_pessoas.append(peso)
    #não quis colocar um monte de condicionais para descobrir o maior e o menor peso, usei as funções prontas do python mesmo

print(f"O maior peso registrado foi de {max(peso_pessoas)} kg.")
print(f"O menor peso registrado foi de {min(peso_pessoas)} kg.")