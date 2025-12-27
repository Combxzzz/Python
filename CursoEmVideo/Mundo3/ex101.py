from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 65:
        return f"com {idade} anos o voto é opcional"
    elif idade >= 18:
        return f"com {idade} anos o voto é obrigatorio"
    elif idade >= 16:
        return f"com {idade} anos o voto nao é obrigatorio"

print(voto(int(input("Digite o ano de nascimento: "))))