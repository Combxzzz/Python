from Projetos.Jogo_RPG.Classes_Players.Classes_Jogadores import Jogador
from Projetos.Jogo_RPG.Colecoes.Magias import MAGIAS

class Mago(Jogador):
    def __init__(self, nome):
        super().__init__(nome, "Mago")
        self.nivel = 1
        self.forca = 5
        self.agilidade = 7
        self.inteligencia = 15
        self.mana = 100
        self.vida_max = 70
        self.vida_atual = self.vida_max

    def usar_magia(self, magia, alvo):
        if magia not in MAGIAS:
            print(f"{self.nome} não conhece a magia {magia}!")
            return

        dados_magia = MAGIAS[magia]

        if self.mana < dados_magia['custo_mana']:
            print(f"{self.nome} não tem mana suficiente para usar {dados_magia['nome']}!")
            return

        if dados_magia['tipo'] == 'dano':
            valor = dados_magia['dano_base'] + (self.inteligencia * 1.2)
        elif dados_magia['tipo'] == 'cura':
            valor = dados_magia['cura_base'] + (self.inteligencia * 1.2)
        else:
            raise ValueError("Tipo de magia desconhecido.")

        if dados_magia['tipo'] == 'dano':
            print(f"{self.nome} usa {dados_magia['nome']} em {alvo.nome}, causando {valor:.1f} de dano!")
            alvo.receber_dano(valor)

        elif dados_magia['tipo'] == 'cura':
            print(f"{self.nome} usa {dados_magia['nome']} em {alvo.nome}, curando {valor:.1f} de vida!")
            alvo.receber_cura(valor)

        self.mana -= dados_magia['custo_mana']
        print(f"{self.nome} agora tem {self.mana} de mana restante.")

    def __str__(self):
        return (f"Mago: {self.nome}, Nível: {self.nivel}, Força: {self.forca}, "
                f"Agilidade: {self.agilidade}, Inteligência: {self.inteligencia}, "
                f"Mana: {self.mana}, Vida: {self.vida_atual}/{self.vida_max}")
