class Telefone:
    agenda = []  # lista compartilhada entre todas as instâncias

    def __init__(self, numero, nome, cep="Brasil"):
        self.numero = numero
        self.nome = nome
        self.cep = cep

    def registrar_numero(self, telefone):
        if not any(t.numero == telefone.numero for t in self.__class__.agenda):
            self.__class__.agenda.append(telefone)
            print(f"Número {telefone.numero} registrado com sucesso para {telefone.nome}.")
        else:
            print(f"Número {telefone.numero} já está registrado na agenda.")

    def remover_numero(self, telefone):
        for t in self.__class__.agenda:
            if t.numero == telefone.numero:
                self.__class__.agenda.remove(t)
                print(f"Número {telefone.numero} removido com sucesso da agenda.")
                return
        print(f"Número {telefone.numero} não encontrado na agenda.")

    @classmethod
    def exibir(cls):
        print("Agenda Telefônica:\n")
        for contato in cls.agenda:
            print(f"Nome: {contato.nome}, \nNúmero: {contato.numero}, \nCEP: {contato.cep}\n"+"-"*20)


    def __repr__(self):
        return f"Telefone(nome={self.nome!r}, numero={self.numero!r}, cep={self.cep!r})"

# Exemplo de uso
telefone1 = Telefone(1234567890, "Alice")
telefone2 = Telefone(9876543210, "Bob")
telefone1.registrar_numero(telefone1)
telefone1.registrar_numero(telefone2)



Telefone.exibir()
