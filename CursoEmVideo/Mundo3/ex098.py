import time

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    print(f"Contagem personalizada de {inicio} ate {fim} de {passo} em {passo}")

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            time.sleep(0.7)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(f'{i} ', end='')
            time.sleep(0.7)

    print()

contador(1, 10, 0)
contador(10, 0, 2)