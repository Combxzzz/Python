def fatorial(numero, show=False):
    """

    :param numero: numero para calcular o fatorial
    :param show: mostrar ou nao a conta do fatorial
    :return: Retorna o valor do fatorial de "numero"
    """
    f = numero
    for i in range(numero - 1, 0, -1):
        f *= i

    if show:
        conta = " x ".join(str(i) for i in range(numero, 0, -1))
        return f"{conta} = {f}"
    else:
        return f

print(fatorial(8, True))
