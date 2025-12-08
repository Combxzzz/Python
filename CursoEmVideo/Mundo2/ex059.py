# while True:
#     n1 = float(input("Digite um numero: "))
#     n2 = float(input("Digite outro numero: "))

#     e = input("""
# [1] Somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# Escolha: """)
    
#     if e == "1":
#         print(f"{n1} + {n2} = {n1 + n2}")
#         break

#     elif e == "2":
#         print(f"{n1} x {n2} = {n1 * n2}")
#         break

#     elif e == "3":
#         if n1 > n2:
#             print(f"{n1} é maio q {n2}")
#             break
#         elif n2 > n1:
#             print(f"{n2} é maio que {n1}")
#             break
#         else:
#             print("Os dois sao iguais")
#             break

#     elif e == "4":
#         continue

#     elif e == "5":
#         exit()
#     else:
#         print("Erro")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))


menu = ""

while menu != "5":

    menu = input("""[1] somar
[2] multi
[3] maior
[4] novos numeros
[5] sair
""")

    if menu == "1":
        print(f"{n1} + {n2} = {n1 + n2}")

    elif menu == "2":
        print(f"{n1} x {n2} = {n1 * n2}")

    elif menu == "3":
        print(f"O maior é {max(n1, n2)}.")

    elif menu == "4":
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite outro numero: "))
    
    elif menu not in ["1", "2", "3", "4", "5"]:
        print("invalido.")

print("finalizando...")