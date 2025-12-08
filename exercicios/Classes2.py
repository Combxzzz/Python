class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic" ,"premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception ("Plano invalido!")

    def mudar_de_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print("oi")
        else:
            print("Plano invalido!")
            print(self)


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme or self.plano == "premium":
            print(f"vendo o filme {filme}")
        else:
            print("voce nao pode ver esse filme! Faça um upgrade para ver esse filme")
        

cliente = Cliente("Teste1", "Teste@email.com", "basic")

print(cliente.plano)
cliente.ver_filme("teste", "premium")

cliente.mudar_de_plano("premium")
cliente.ver_filme("teste", "premium")
        