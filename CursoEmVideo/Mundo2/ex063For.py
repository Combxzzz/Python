termos = int(input("Digite quantos termos voce quer mostrar: "))

termo1 = 0
termo2 = 1

print(f"{termo1} -> {termo2} -> ", end='')

for i in range(termos - 2, 0, -1):
    soma = termo1 + termo2
    termo1 = termo2
    termo2 = soma
    print(soma, end=' -> ')

print("FIM")
print(f"esses sao os {termos} termos da sequencia de fibonacci.")
