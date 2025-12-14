from magias import MAGIAS

class Jogador:

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
            print(f"{self.nome} usa {dados_magia['nome']} em si mesmo, curando {valor:.1f} de vida!")
            self.receber_cura(valor)

        self.mana -= dados_magia['custo_mana']
        print(f"{self.nome} agora tem {self.mana} de mana restante.")


    def __repr__(self):
        return f"Jogador(nome={self.nome}, classe={self.classe}, nivel={self.nivel}, vida={self.vida_atual}, mana={self.mana})"
