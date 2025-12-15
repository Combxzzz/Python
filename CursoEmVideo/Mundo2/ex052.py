numero = int(input("Digite um número para saber se ele é primo: "))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f"\033[34m{c}\033[m", end=' ')
        total += 1
    else:
        print(f"\033[31m{c}\033[m", end=' ')

if numero % 2 == 0 and numero != 2:
    print(f"\nO número {numero} não é primo!")
else:
    print(f"\nO número {numero} é primo!")

print(f"O número {numero} foi divisível {total} vezes.")
if total == 2:
    print("Portanto, ele é primo!")
else:
    print("Portanto, ele não é primo!")