import random

class Goblin:
    def __init__(self, nome = "Goblin"):
        self.nome = nome
        self.vida = 100
        self.forca = random.randint(3, 6)
        self.agilidade = random.randint(2, 5)
        self.inteligencia = random.randint(1, 3)

    def atacar(self, alvo):
        dano = self.forca * 1.4
        print(f"{self.nome} ataca {alvo.nome} causando {dano:.2f} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano e foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    def __repr__(self):
        return f"Goblin(nome={self.nome}, vida={self.vida})"
