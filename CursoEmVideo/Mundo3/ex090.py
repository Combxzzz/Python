aluno = dict()

aluno['nome'] = str(input("Digite o nome do aluno: "))
aluno['media'] = float(input("Digite a medida do aluno: "))
aluno['situacao'] = "aprovado" if aluno['media'] >= 6 else "reprovado"

print(f"Nome do aluno: {aluno['nome']}")
print(f"Media do aluno: {aluno['media']}")
print(f"Situação atual do aluno: {aluno['situacao']}")