class Jogador:

    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 0
        self.forca = 0
        self.agilidade = 0
        self.inteligencia = 0
        self.vida_max = 0
        self.vida_atual = self.vida_max

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


    def __str__(self):
        return (f"Mago: {self.nome}, Nível: {self.nivel}, Força: {self.forca}, "
                f"Agilidade: {self.agilidade}, Inteligência: {self.inteligencia}, "
                f"Mana: {self.mana}, Vida: {self.vida_atual}/{self.vida_max}")
