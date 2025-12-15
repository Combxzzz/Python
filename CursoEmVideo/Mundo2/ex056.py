media_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
total_mulheres_menores_20 = 0

for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    media_idades += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            homem_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            total_mulheres_menores_20 += 1

print(f"A média de idade do grupo é de {media_idades / 4:.1f} anos.")
if homem_mais_velho:
    print(f"O homem mais velho é {homem_mais_velho} com {idade_homem_mais_velho} anos.")
print(f"Ao todo são {total_mulheres_menores_20} mulheres com menos de 20 anos.")