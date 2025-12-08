sexo = str(input("Digite seu sexo [M/F]: ")).upper()

while sexo not in ["M","F"]:
    sexo = str(input("invalido.\ndigite seu sexo novamente [M/F]: ")).upper()

if sexo == "F":
    print("Voce é mulher.")
else:
    print("Voce é homem.")