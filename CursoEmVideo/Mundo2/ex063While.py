termos = int(input("Digite quantos termos voce quer mostrar: "))
termo1 = 0
termo2 = 1

contador = 2
print(f"{termo1} -> {termo2} -> ", end='')

while contador < termos:
    soma = termo1 + termo2
    termo1 = termo2
    termo2 = soma
    print(soma, end=' -> ')
    contador += 1

print("FIM")
print(f"esses sao os {termos} termos da sequencia de fibonacci.")
