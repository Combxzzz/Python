from Classes_Monstros import *
from Classes_Jogadores import *

# exemplo de uso
jogador1 = Jogador("Aragorn", "Guerreiro")
goblin1 = Goblin("Goblin Malvado")
jogador1.atacar(goblin1)
goblin1.atacar(jogador1)
jogador1.usar_magia("relampago", goblin1)
jogador1.usar_magia("cura", jogador1)

print(jogador1)
print(goblin1)