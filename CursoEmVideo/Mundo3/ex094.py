pessoas = {
    'pessoas' : [],
    'idades' : [],
    'sexo' : []
}

while True:
    nome = str(input("Digite o nome da pessoa: ")).title().strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo da pessoa [F/M]: ")).upper()[0]
    pessoas['pessoas'].append(nome)
    pessoas['idades'].append(idade)
    pessoas['sexo'].append(sexo)
    opcao = str(input("Quer continuar? [S/N] ")).upper()[0]

    while opcao not in 'SN':
        opcao = str(input("Quer continuar? [S/N] ")).upper()[0]
    if opcao == 'N':
        break

media = sum(pessoas['idades']) / len(pessoas['idades'])

print(pessoas)
print(f"O grupo tem {len(pessoas['pessoas'])} pessoas")
print(f"A media de idades é: {media:.2f}")
print("As mulheres cadastradas foram:", end=" ")
for index, sexo in enumerate(pessoas['sexo']):
    if sexo == 'F':
        print(pessoas['pessoas'][index], end=" ")
print()

print("Pessoas acima de media de idade:\n")
for index, idade in enumerate(pessoas['idades']):
    if idade > media:
        print(f"Nome: {pessoas['pessoas'][index]}; "
              f"Sexo: {pessoas['sexo'][index]}; "
              f"Idade: {pessoas['idades'][index]}\n")
print()