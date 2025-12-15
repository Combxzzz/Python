numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.remove(2)

posicao = numeros.index(4)
numeros.insert(posicao, 40)
numeros.remove(4)

numeros.sort(reverse=True)
print(numeros)