import datetime

nasci = int(input("Em qual ano voce nasceu: "))
agora = datetime.datetime.now()
ano = agora.year
idade = ano - nasci

if idade <= 9:
    print("mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print("junior")
elif idade <= 20:
    print("senior")
else:
    print("master")
    
print(idade)