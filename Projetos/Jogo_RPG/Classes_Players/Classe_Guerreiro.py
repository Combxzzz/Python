from Projetos.Jogo_RPG.Classes_Players.Classes_Jogadores import Jogador
from Projetos.Jogo_RPG.Colecoes.Habilidades import HABILIDADES

class Guerreiro(Jogador):
    def __init__(self, nome):
        super().__init__(nome, "Guerreiro")
        self.nivel = 1
        self.forca = 15
        self.agilidade = 10
        self.inteligencia = 5
        self.energia = 65
        self.vida_max = 120
        self.vida_atual = self.vida_max

    def usar_habilidade(self, habilidade, alvo):
        if habilidade not in HABILIDADES:
            print(f"{self.nome} não conhece a habilidade {habilidade}!")
            return

        dados_habilidade = HABILIDADES[habilidade]

        if self.energia < dados_habilidade['custo_energia']:
            print(f"{self.nome} não tem energia suficiente para usar {dados_habilidade['nome']}!")
            return

        if dados_habilidade['tipo'] == 'dano':
            valor = dados_habilidade['dano_base'] + (self.forca * 1.2)

        elif dados_habilidade['tipo'] == 'atribuicao':
            valor = dados_habilidade['vida+']

        elif dados_habilidade['tipo'] == 'cura':
            valor = dados_habilidade['cura_base'] + (self.forca * 1.2)

        else:
            raise ValueError("Tipo de habilidade desconhecido.")

        if dados_habilidade['tipo'] == 'dano':
            print(f"{self.nome} usa {dados_habilidade['nome']} em {alvo.nome}, causando {valor:.1f} de dano!")
            alvo.receber_dano(valor)


        elif dados_habilidade['tipo'] == 'atribuicao':
            print(f"{self.nome} usa {dados_habilidade['nome']}, aumentando sua vida!")
            self.vida_max += valor
            self.vida_atual += valor

            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max

            print(f"{self.nome} agora tem {self.vida_atual} de vida, com {self.vida_max} de vida máxima!")

        self.energia -= dados_habilidade['custo_energia']
        print(f"{self.nome} agora tem {self.energia} de energia restante.")

    def __str__(self):
        return (f"Guerreiro: {self.nome}, Nível: {self.nivel}, Força: {self.forca}, "
                f"Agilidade: {self.agilidade}, Inteligência: {self.inteligencia}, "
                f"Energia: {self.energia}, Vida: {self.vida_atual}/{self.vida_max}")