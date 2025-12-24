jogador = {
    'nome': [],
    'gols': [],
    'total': []
}

while True:
    nome = input("Qual o nome do jogador? ").title()
    partidas = int(input(f"Quantas partidas {nome} jogou: "))

    jogador['nome'].append(nome)

    golsPorPartida = []
    for i in range(1, partidas + 1):
        golsPorPartida.append(int(input(f"Quantos gols na partida {i}? ")))

    jogador['gols'].append(golsPorPartida)
    jogador['total'].append(sum(golsPorPartida))

    opcao = input("Continuar [S/N]: ").upper()[0]
    while opcao not in "SN":
        opcao = input("Continuar [S/N]: ").upper()[0]
    if opcao == "N":
        break


print("-" * 55)
print(f"{'ID.':<5}{'NOME':<16}{'GOLS':<20}{'TOTAL':<10}")
print("-" * 55)


for i in range(len(jogador['nome'])):
    print(f"{i:<5}"
          f"{jogador['nome'][i]:<16}"
          f"{str(jogador['gols'][i]):<20}"
          f"{jogador['total'][i]:<10}")

print("-" * 55)

while True:
    id_jogador = int(input("Mostrar dados de qual jogador? (999 para sair): "))

    if id_jogador == 999:
        print("Encerrando consulta.")
        break

    if id_jogador < 0 or id_jogador >= len(jogador['nome']):
        print("ID inválido.")
        continue

    print(f"Levantamento do jogador {jogador['nome'][id_jogador]}:")
    for i, gols in enumerate(jogador['gols'][id_jogador], start=1):
        print(f"  Na partida {i}, fez {gols} gols.")