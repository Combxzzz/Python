from Projetos.Jogo_RPG.Classes_Players.Classe_Guerreiro import Guerreiro
from Projetos.Jogo_RPG.Classes_Players.Classe_Mago import Mago
from Projetos.Jogo_RPG.Classes_Monstros.Classes_Monstros import Goblin

# exemplo de uso
guerreiro = Guerreiro("Thorin")
mago = Mago("Gandalf")
gobrin = Goblin("Gobrin Ferox")

guerreiro.usar_habilidade("golpe_forte", gobrin)
gobrin.atacar(guerreiro)
mago.usar_magia("cura", guerreiro)

# ainda em desenvolvimento
