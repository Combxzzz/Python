# Projeto: Concatenar idades únicas com a próxima idade na lista

# pega uma lista de idades em inteiros e converte para strings
lista_de_idades_inteiros = [12, 54, 53, 14, 23, 45, 67, 8, 9, 90, 34]
lista_de_idades_em_str = [str(x) for x in lista_de_idades_inteiros]

# definição do índice inicial e do tamanho da lista
i = 0
n = len(lista_de_idades_em_str)

# percorre a lista de idades em strings
while i < n:
    # pega o valor atual
    cur = lista_de_idades_em_str[i]

    # verifica se o valor atual é um dígito único e se há um próximo valor
    if len(cur) == 1 and i + 1 < n:

        # concatena o dígito único com o próximo
        print(cur + lista_de_idades_em_str[i + 1])

        # avança o índice em 2 posições porque dois valores foram processados
        i += 2

    else:
        # apenas imprime o valor atual
        print(cur)

        # avança o índice em 1 posição porque apenas um valor foi processado
        i += 1
