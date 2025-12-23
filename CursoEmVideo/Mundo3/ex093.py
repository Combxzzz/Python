jogador = {
    'nome' : '',
    'gols' : [],
    'total' : 0,
}

nome = str(input("Qual o nome do jogador? ")).title()
partidas = int(input(f"Quantas partidas {nome} jogou: "))
jogador['nome'] = nome


for i in range(1, partidas + 1):
    golsPorPartida = int(input(f"Quantos gols na partida {i}? "))
    jogador['gols'].append(golsPorPartida)
    jogador['total'] += golsPorPartida

print("-" * 45)
print(jogador)
print("-" * 45)


print(f"Nome: {jogador['nome']}")
print(f"Gols: {jogador['gols']}")
print(f"Total: {jogador['total']}")

print("-" * 45)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for p, g in enumerate(jogador['gols']):
    print(f"    Na partida {p + 1}, fez {g} gols")
print(f"Foi um total de {jogador['total']} gols")