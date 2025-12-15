n1 = int(input("Digite um numero: "))
# final = f"esse são os {n1 + 2} primeiros termos de uma sequencia de fibonacci."


a = 0
b = 1

print(a)
print(b)

# while n1 > 0:
#     c = a + b
#     a = b
#     b = c
#     n1 -= 1
#     print (c)

# print(final)

for i in range(n1, 0, -1):
    c = a + b
    a = b
    b = c
    print (c)

# print(final)
print(f"esses sao os {n1 + 2} termos da sequencia.")

# Que codigo feio meu Deus do ceu
# Bom saber que eu sai disso aqui pra oque ta nos outros ex63 💀
# Deixar aqui so pra lembrar que eu realmente melhorei