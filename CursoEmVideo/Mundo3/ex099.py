from time import sleep

def maior(*numeros):
    for i in numeros:
        print(f'{i} ', end='')
    print()
    print(f"Foram informado {len(numeros)} valores ao todo")
    print(f"O maior valor informado foi {max(numeros)}")
    sleep(0.7)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)