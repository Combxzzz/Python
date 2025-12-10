velo = float(input('Qual a velocidade atual do carro? '))

if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você foi multado por excesso de velocidade! Sua multa é de R$ {multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')