valor = int(input("Valor que deseja sacar: "))

notas_de_50 = valor // 50
if notas_de_50 > 0:
    print(f"Total de {notas_de_50} notas de R$50")
    valor -= notas_de_50 * 50

notas_de_20 = valor // 20
if notas_de_20 > 0:
    print(f"Total de {notas_de_20} notas de R$20")
    valor -= notas_de_20 * 20

notas_de_10 = valor // 10
if notas_de_10 > 0:
    print(f"Total de {notas_de_10} notas de R$10")
    valor -= notas_de_10 * 10

notas_de_1 = valor // 1
if notas_de_1 > 0:
    print(f"Total de {notas_de_1} notas de R$1")

# Totalmente diferente da do guanabara slk, não usei nem while
# isso é uma coisa ruim?