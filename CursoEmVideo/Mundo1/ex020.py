from random import shuffle
alunos = []

for i in range(0, 4):
    aluno = str(input("Digite o nome do aluno: "))
    alunos.append(aluno)

shuffle(alunos)
print(f"A ordem de apresentação será:{alunos}")