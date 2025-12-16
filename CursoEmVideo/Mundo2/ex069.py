mais_18 = homens = mulheres_menos_20 = 0

while True:
    print("-" * 20)
    print("Cadastro de pessoa")
    print("-" * 20)

    idade = int(input("Idade: "))

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if idade > 18:
        mais_18 += 1
    elif sexo == "M":
        homens += 1
    elif sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
    else:
        continue

print(f"Total de pessoas com mais de 18 anos: {mais_18}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menos_20}")