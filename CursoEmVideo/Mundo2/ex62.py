primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
limite = 10
termo_atual = primeiro_termo
contador = 0

while contador < limite:
    print(termo_atual, end=' -> ')
    termo_atual += razao
    contador += 1

    if contador == limite:
        print('PAUSA')
        quantidade_mais = int(input("\nDeseja ver mais termos? Quantos? "))
        limite += quantidade_mais
        if quantidade_mais == 0:
            break


print(f"Foram mostrados {contador} termos da PA.")

# meu jeito fico um pouco diferente mas funciona