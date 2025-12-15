from datetime import date

maior_idade = 0
menor_idade = 0

for i in range(1, 8):
    nascimento = int(input(f'Em que ano a {i}a pessoa nasceu? '))
    idade_atual = date.today().year - nascimento
    if idade_atual >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f"Ao todo tivemos {maior_idade} pessoas maiores de idade.")
print(f"E também tivemos {menor_idade} pessoas menores de idade.")