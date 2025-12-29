# Aula23 - Tratamento de Erros e Exceções em Python

# ---------------------------------------------------------
# Nessa aula aprendemos:
# - o que são erros
# - o que são exceções
# - como usar try / except
# - else e finally
# ---------------------------------------------------------

# ---------------------------------------------------------
# EXEMPLO SEM TRATAMENTO DE ERRO
# ---------------------------------------------------------
# Se o usuário digitar algo errado, o programa quebra

# num = int(input("Digite um número: "))
# print(num)

# ---------------------------------------------------------
# USANDO TRY / EXCEPT
# ---------------------------------------------------------

try:
    num = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {num}")
except:
    print("Erro! Você não digitou um número inteiro válido.")

# ---------------------------------------------------------
# TRATANDO ERROS ESPECÍFICOS
# ---------------------------------------------------------

try:
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    r = a / b
except ValueError:
    print("Erro! Digite apenas números inteiros.")
except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.")
else:
    # só executa se não houver erro
    print(f"O resultado da divisão é {r}")
finally:
    # sempre executa
    print("Fim do programa.")

# ---------------------------------------------------------
# EXEMPLO COM LOOP E VALIDAÇÃO
# ---------------------------------------------------------

while True:
    try:
        n = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
    else:
        print(f"Número válido digitado: {n}")
        break

# ---------------------------------------------------------
# EXEMPLO COM FUNÇÃO E TRY / EXCEPT
# ---------------------------------------------------------

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero"
    except TypeError:
        return "Erro: tipo de dado inválido"

print(dividir(10, 2))
print(dividir(10, 0))
print(dividir(10, "a"))

# ---------------------------------------------------------
# DICA IMPORTANTE
# ---------------------------------------------------------
# Evite usar "except:" sozinho
# Prefira tratar exceções específicas
# Isso deixa o código mais seguro
