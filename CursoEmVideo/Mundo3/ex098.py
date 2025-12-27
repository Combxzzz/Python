import time

def contador(inicio, fim, passo=0):
    if passo == 0:
        passo = 1

    print(f"Contagem personalizada de {inicio} ate {fim} de {passo} em {passo}")

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            time.sleep(0.5)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i} ', end='')
            time.sleep(0.5)

    print()

contador(1, 10, 0)
contador(10, 0, 2)

print("personalize a sua contagem: ")
ini = int(input("Inicio: "))
fin = int(input("Fim: "))
passo = int(input("Passo: "))

contador(ini, fin, passo)
