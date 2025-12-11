import datetime

nascimento = int(input("Insira o ano de nascimento: "))
sexo = input("Insira o sexo (M/F): ").strip().upper()
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

while True:
    if sexo == "M":
        if idade < 18:
            restante = 18 - idade
            ano_alistamento = ano_atual + restante
            print(f"Quem nasceu em {nascimento} tem {idade} em {ano_atual}.")
            print(f"Falta {restante} ano para o seu alistamento." if restante == 1 else f"Faltam {restante} anos para o seu alistamento.")
            print(f"Seu alistamento será em {ano_alistamento}.")

        elif idade == 18:
            print(f"Quem nasceu em {nascimento} tem {idade} em {ano_atual}.")
            print(f"Voce ja deve ter se alistado ou deve se alistar esse ano.")

        else:
            passado = idade - 18
            ano_alistamento = ano_atual - passado
            print(f"Quem nasceu em {nascimento} tem {idade} em {ano_atual}.")
            print(f"Voce ja deveria ter se alistado ha {passado} ano." if passado == 1 else f"Voce ja deveria ter se alistado ha {passado} anos.")
            print(f"Seu alistamento foi em {ano_alistamento}.")
    elif sexo == "F":
        print("O alistamento militar não é obrigatório para mulheres.")
    else:
        print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
        sexo = input("Insira o sexo (M/F): ").strip().upper()
        continue
    break
