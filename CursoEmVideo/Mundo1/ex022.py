nome = input("Digite seu nome completo: ").strip()

print("\nAnalisando seu nome...")

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome.replace(' ', ''))} letras")

partes = nome.split()
primeiro = partes[0]

print(f"Seu primeiro nome é {primeiro} e ele tem {len(primeiro)} letras")

#Dei uma melhorada no código para evitar contar os espaços no total de letras do nome.