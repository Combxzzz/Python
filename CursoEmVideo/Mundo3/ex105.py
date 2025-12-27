def notas(*n, sit=False):
    """

    :param n: notas do aluno(pode colocar varias notas)
    :param sit: exibir a situacao do aluno
    :return: retorna um dic com todas as informações do aluno
    """
    media = sum(n) / len(n)
    resultado = {
        'total' : len(n),
        'maior' : max(n),
        'menor' : min(n),
        'media' : media,
    }
    if sit:
        resultado['situacao'] = "BOA" if media >= 7 else "RUIM"
    return resultado


aluno = notas(5.5, 9.5, 10, 6.5, sit=True)
aluno2 = notas(5.5, 2, 5, 1.5, sit=False)
help(notas)

print(aluno)
print(aluno2)