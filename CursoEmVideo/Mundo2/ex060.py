n1 = int(input("Digite um numero: "))
mult = 1

# while n1 > 0:
#     mult = mult * n1
#     n1 -= 1

# print(mult)


for i in range(n1, 0, -1):
    mult *= i

print(mult)