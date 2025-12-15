palavra = str(input('Digite uma palavra: ')).strip().upper().split()
junto = ''.join(palavra)
inverso = ''
# Voce pode usar inverso = [::-1] para inverter a string, mas aqui está o método com loop

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}.')
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A palavra digitada não é um palíndromo!')