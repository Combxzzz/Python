nums = 0 

for i in range(1, 7):
    r = int(input("Digite um numero: "))
    if r % 2 == 0:
        nums += r

print(f"A soma é {nums}")