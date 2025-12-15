primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo_atual = primeiro_termo
contador = 0

while contador < 10:
    print(termo_atual, end=' -> ')
    termo_atual += razao
    contador += 1
print("FIM")