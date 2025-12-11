# Aula14 - Estruturas de Repetição While

# -------------------------------------------------------------------
# Na aula 14 aprendemos a repetir ações enquanto uma condição for verdadeira.
# O WHILE é útil quando você NÃO sabe quantas vezes a repetição vai acontecer.
#
# Estrutura:
# while condição:
#     comando
# -------------------------------------------------------------------

# Exemplo 1 — Contando até 10 usando while
print("Contando até 10 com WHILE:")
contador = 1  # variável de controle

while contador <= 10:  # enquanto contador for <= 10
    print(contador)
    contador += 1  # incrementa para evitar loop infinito

print("FIM!\n")

# -------------------------------------------------------------------
# Exemplo 2 — Repetição com condição de parada (flag)
# -------------------------------------------------------------------
print("Digite números e eu somo. Digite 0 para parar.")

num = int(input("Digite um número: "))
soma = 0  # acumulador

while num != 0:     # 0 será o número de parada (flag)
    soma += num
    num = int(input("Digite outro número (0 para parar): "))

print(f"A soma total foi {soma}.\n")

# -------------------------------------------------------------------
# Exemplo 3 — Contando quantos números foram digitados
# -------------------------------------------------------------------
print("Agora vamos contar quantos números você digitou (0 para parar).")

quantidade = 0
num = int(input("Digite um número: "))

while num != 0:
    quantidade += 1
    num = int(input("Digite outro número (0 para parar): "))

print(f"Você digitou {quantidade} números!\n")

# -------------------------------------------------------------------
# Exemplo 4 — Validando entrada com while
# -------------------------------------------------------------------
# WHILE é muito usado para validar dados

sexo = input("Digite seu sexo [M/F]: ").strip().upper()

# enquanto a resposta NÃO for 'M' E também NÃO for 'F'
while sexo != "M" and sexo != "F":
    print("Opção inválida! Tente novamente.")
    sexo = input("Digite seu sexo [M/F]: ").strip().upper()

print(f"Sexo registrado com sucesso: {sexo}\n")

# -------------------------------------------------------------------
# Exemplo 5 — WHILE com interrupção usando break
# -------------------------------------------------------------------
print("Exemplo com BREAK (encerra o while imediatamente):")

contador = 1
while True:  # loop infinito
    print(contador)
    contador += 1
    if contador > 5:  # quando passar de 5, o break PARA o while
        break

print("Loop interrompido com break!\n")
