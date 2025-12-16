# Aula15 - Interrompendo Repetições em Python

# -------------------------------------------------------------------
# Nesta aula aprendemos a usar:
# - while True
# - break
#
# O break serve para ENCERRAR um laço de repetição imediatamente.
# Ele pode ser usado tanto no for quanto no while.
# -------------------------------------------------------------------

# Exemplo 1 — Loop infinito controlado com break
print("Digite números para somar (999 para parar).")

soma = 0            # acumulador
contador = 0        # conta quantos números foram digitados

while True:         # loop infinito
    num = int(input("Digite um número: "))

    # 999 é o valor sentinela (flag de parada)
    if num == 999:
        break       # encerra o while

    soma += num     # soma os valores digitados
    contador += 1   # conta quantos números foram digitados

print(f"Você digitou {contador} números.")
print(f"A soma entre eles foi {soma}.\n")

# -------------------------------------------------------------------
# Exemplo 2 — Usando break em um FOR
# -------------------------------------------------------------------

print("Contagem com interrupção:")

for c in range(1, 11):
    if c == 6:      # quando chegar no 6
        break       # o laço é interrompido
    print(c)

print("Loop FOR interrompido!\n")

# -------------------------------------------------------------------
# Exemplo 3 — break com validação de dados
# -------------------------------------------------------------------
print("Digite seu sexo [M/F] (0 para sair):")

while True:
    sexo = input("Sexo: ").strip().upper()

    # condição para sair do loop
    if sexo == "0":
        print("Programa encerrado.")
        break

    # validação do valor digitado
    if sexo == "M" or sexo == "F":
        print("Sexo registrado com sucesso!\n")
    else:
        print("Valor inválido! Tente novamente.\n")

# -------------------------------------------------------------------
# Exemplo 4 — Usando continue
# -------------------------------------------------------------------
# continue pula para a próxima repetição do laço

print("Exemplo usando CONTINUE:")

for n in range(1, 11):
    if n % 2 == 0:
        continue    # pula os números pares
    print(n)        # imprime apenas os ímpares

print("\nFIM DA AULA 15")
