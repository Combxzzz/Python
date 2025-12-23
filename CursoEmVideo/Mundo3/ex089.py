alunos = []

while True:
    nome = str(input("Nome: ")).title()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    alunos.append([nome, [nota1, nota2]])

    opcao = str(input("Deseja continuar? [S/N] ")).upper()
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? [S/N] ")).upper()
    if opcao == "N":
        break

print(alunos)

print("-" * 40)
print(f"{'No.':<4}{'NOME':<15}{'MÉDIA':>6}")
print("-" * 40)

for i, aluno in enumerate(alunos):
    media = sum(aluno[1]) / len(aluno[1])
    print(f"{i+1:<4}{aluno[0]:<15}{media:>6.2f}")

print("-"*45)

while True:
    id_aluno = int(input("Digite o id do aluno para mostrar as notas(999 para parar): "))
    if id_aluno == 999:
        break
    print(f"Notas do aluno {alunos[id_aluno - 1][0]}: {alunos[id_aluno - 1][1]}")