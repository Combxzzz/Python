class Criar_usuario():
    def __init__(self):
        self.user = ""
        self.email = ""
        self.senha = ""

    def reg_user(self, user):
        self.user = user

    def reg_email(self, email):
        self.email = email
    
    def reg_senha(self, password):
        self.senha = password

    def __str__(self):
        email = self.email or "Não informado"
        senha = self.senha or "Nao informado"
        usuario = self.user or "Não informado"
        return f"Usuario: {usuario} | Email: {email} | Senha: {senha}"

usuario = Criar_usuario()
usuario.reg_user(str(input("Digite seu Usuario: ")))
usuario.reg_email(str(input("Digite seu Email: ")))
usuario.reg_senha(str(input("Digite sua Senha: ")))

print(usuario)