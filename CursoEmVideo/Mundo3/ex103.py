def ficha(jogador= "<Desconhecido>", gols=0):
    return f"O jogador {jogador} fez {gols} gol(s)"

jogado = ficha(jogador=str(input('Nome do jogador: ')), gols=int(input('Quantos gols na partida: ')))

print(jogado)
