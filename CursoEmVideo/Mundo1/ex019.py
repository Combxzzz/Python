from random import choice
alunos = []

for i in range(0, 4):
    aluno = str(input("Digite o nome do aluno: "))
    alunos.append(aluno)

escolhido = choice(alunos)
print(f"O aluno escolhido foi {escolhido}")