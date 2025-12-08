num = int(input("Digite um numero inteiro: "))

while True:
    escolha = int(input("""
Escolha uma base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
"""))
        
    if escolha == 1:
        print(bin(num)[2:])
        break
    elif escolha == 2:
        print(oct(num)[2:])
        break
    elif escolha == 3:
        print(hex(num)[2:])
        break
    else:
        print("\nDigite um opçao valida...")    
print("encerrando programa...")