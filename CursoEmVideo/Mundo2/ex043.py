peso = float(input("Digite o peso kg: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} e você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f} e você está com o peso ideal.")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f} e você está com sobrepeso.")
elif 30 <= imc < 40:
    print(f"Seu IMC é {imc:.2f} e você está com obesidade.")
else:
    print(f"Seu IMC é {imc:.2f} e você está com obesidade mórbida.")