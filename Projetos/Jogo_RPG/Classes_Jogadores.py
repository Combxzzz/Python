class Jogador:
    magias_de_dano = {
        'bola_de_fogo': {'nome': 'Bola de Fogo', 'dano': 30, 'custo_mana': 10, 'tipo': 'dano'},
        'raio_de_gelo': {'nome': 'Raio de Gelo', 'dano': 25, 'custo_mana': 8, 'tipo': 'dano'},
        'relampago': {'nome': 'Relâmpago', 'dano': 35, 'custo_mana': 12, 'tipo': 'dano'},
        'cura' : {'nome': 'Cura', 'cura': 40, 'custo_mana': 15, 'tipo': 'cura'}
    }

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 0
        self.forca = 6
        self.agilidade = 5
        self.inteligencia = 5
        self.mana = 20
        self.vida_max = 100
        self.vida_atual = 100

    def atacar(self, alvo):
        dano = self.forca * 1.5
        print(f"{self.nome} ataca {alvo.nome} causando {dano:.2f} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida_atual -= dano
        if self.vida_atual <= 0:
            self.vida_atual = 0
            print(f"{self.nome} recebeu {dano:.1f} de dano e foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano:.1f} de dano. Vida restante: {self.vida_atual}")

    def receber_cura(self, cura):
        if self.vida_atual <= 0:
            print(f"{self.nome} não pode ser curado, pois está derrotado!")
            return
        elif self.vida_atual >= self.vida_max:
            print(f"{self.nome} já está com a vida cheia!")
            return
        else:
            self.vida_atual += cura
            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max

            print(f"{self.nome} recebeu {cura:.1f} de cura. Vida atual: {self.vida_atual}")

    def usar_magia(self, magia, alvo):
        dados_magia = self.magias_de_dano[magia]
        if dados_magia['tipo'] == 'dano':
            if magia in self.magias_de_dano:

                dano = dados_magia['dano'] + self.inteligencia * 1.2
                self.mana -= dados_magia['custo_mana']

                print(f"{self.nome} usa {dados_magia['nome']} em {alvo.nome}, causando {dano:.2f} de dano!")
                alvo.receber_dano(dano)
            else:
                print(f"{self.nome} não conhece essa magia!")
        elif dados_magia['tipo'] == 'cura':
            if magia in self.magias_de_dano:
                cura = dados_magia['cura'] + self.inteligencia * 1.2
                self.mana -= dados_magia['custo_mana']

                alvo.receber_cura(cura)
                print(f"{self.nome} usa {dados_magia['nome']} e recupera {cura:.2f} de vida! Vida atual: {self.vida_atual}")
            else:
                print(f"{self.nome} não conhece essa magia!")

    def exibir_descricao_magia(self, magia):
        if magia in self.magias_de_dano:
            mag = self.magias_de_dano[magia]
            print(f"Magia: {mag['nome']}, Dano: {mag['dano']}, Custo de Mana: {mag['custo_mana']}")
        else:
            print(f"{self.nome} não conhece a magia {magia}!")

    def __repr__(self):
        return f"Jogador(nome={self.nome}, classe={self.classe}, nivel={self.nivel}, vida={self.vida_atual}, mana={self.mana})"

def mudar_de_classe(jogador, nova_classe):
    jogador.classe = nova_classe
    if nova_classe == "Guerreiro":
        jogador.forca += 4
        jogador.vida_max += 20
        jogador.vida_atual = jogador.vida_max
    elif nova_classe == "Mago":
        jogador.inteligencia += 4
        jogador.mana += 15
    elif nova_classe == "Arqueiro":
        jogador.agilidade += 4
        jogador.forca += 2
    else:
        print(f"Classe {nova_classe} desconhecida. Nenhuma alteração feita.")