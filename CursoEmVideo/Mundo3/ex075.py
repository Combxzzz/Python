from collections import Counter

numeros = (
    int(input("Digite um numero: ")),
    int(input("Digite mais um numero: ")),
    int(input("Digite mais outro numero: ")),
    int(input("Digite o ultimo numero: "))
)

contagem = Counter(numeros)

for numero, vezes in contagem.items():
    if vezes >= 2:
        print(f"O numero {numero} apareceu {vezes}")

# Pensei que o guanabara queria saber o numero variavel nao um fixo, tipo, quantas vezes aparece 3
