from datetime import date

pessoas = dict()
ano_atual = date.today().year

nome = str(input('Digite o nome da pessoa: ')).title()
nascimento = int(input('Digite a data de nascimento da pessoa: '))
CTPS = str(input("Tem carteira de trabalho? [S/N]: ")).upper()[0]

pessoas['nome'] = nome
pessoas['idade'] = ano_atual - nascimento
pessoas['CTPS'] = CTPS

if CTPS == 'S':
    ano_contratacao = int(input("Ano de contratacao: "))
    salario = float(input("Salario: "))

    aposentadoria = ano_contratacao + 35
    pessoas['ano_contratacao'] = ano_contratacao
    pessoas['salario'] = salario
    pessoas['aposentadoria'] = aposentadoria - nascimento


print(pessoas)
print(f"Nome: {pessoas['nome']}")
print(f"Idade: {pessoas['idade']}")
print(f"CTPS: {pessoas['CTPS']}")

if pessoas['CTPS'] == 'S':
    print(f"Contratação: {pessoas['ano_contratacao']}")
    print(f"Salario: {pessoas['salario']}")
    print(f"Aposentadoria: {pessoas['aposentadoria']}")