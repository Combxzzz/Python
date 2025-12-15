class Canal:
    def __init__(self, nome, inscritos, descricao, comentario):
        self.nome = nome
        self.inscritos = inscritos        
        self.descricao = descricao
        self.comentario = comentario

    def escrever_se(self, quantidade):
        self.inscritos += quantidade

    def mudar_descricao(self, nova_descricao):
        self.descricao = nova_descricao


    def __str__(self):
        return f"Nome: {self.nome} | Inscritos: {self.inscritos} | Descrição: {self.descricao}"
    


MTG = Canal("MTG", 0, "puro suco do entretenimento", "teste de comentario")

print(MTG)

MTG.escrever_se(5)
MTG.mudar_descricao("gameplays legais👍")

print(MTG)
