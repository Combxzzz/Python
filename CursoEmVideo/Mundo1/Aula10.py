# Aula10 - Estruturas Condicionais (if, else, elif)


# Usamos if/elif/else para fazer verificações e executar blocos diferentes.

# Variavel para armazenar a velocidade do carro
velocidade = int(input("Qual é a velocidade atual do carro? "))

# ---------------------------------------------------------
# CONDIÇÃO SIMPLES
# ---------------------------------------------------------
# if: roda SOMENTE se a condição for verdadeira
# neste caso, se a velocidade for maior que 80, o motorista será multado

if velocidade > 80:
    print("Você foi MULTADO por exceder o limite de velocidade!")

    # calculando o valor da multa
    multa = (velocidade - 80) * 7  # R$7 por km acima do limite
    print(f"Valor da multa: R${multa:.2f}")

# mensagem independente da condição
print("Tenha um bom dia! Dirija com segurança.")

# ---------------------------------------------------------
# CONDIÇÃO COMPOSTA (if + else)
# ---------------------------------------------------------

idade = int(input("\nDigite sua idade: "))

# verifica se a pessoa é maior de idade
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# ---------------------------------------------------------
# CONDIÇÃO ENCADEADA (if + elif + else)
# ---------------------------------------------------------
# vários testes na mesma estrutura

print("\n--- Testando média escolar ---")
nota = float(input("Digite sua média final: "))

if nota >= 7:
    print("APROVADO!")
elif 5 <= nota < 7:
    print("RECUPERAÇÃO!")
else:
    print("REPROVADO!")

# ---------------------------------------------------------
# OPERADOR TERNÁRIO (condição simplificada)
# ---------------------------------------------------------

# aqui verificamos se um número é par ou ímpar
numero = int(input("\nDigite um número: "))
resultado = "PAR" if numero % 2 == 0 else "ÍMPAR"

print(f"O número {numero} é {resultado}.")

# ---------------------------------------------------------
# VÁRIAS CONDIÇÕES COM 'in' E 'not in' (geralmente usadas com listas)
# ---------------------------------------------------------

# pedindo o nome
nome = input("\nDigite seu nome: ").strip()

# nomes especiais
nomes_legais = ["Vinicius", "Maria", "João", "Pedro"]

if nome in nomes_legais:
    print("Seu nome é bem comum e legal!")
else:
    print("Seu nome é diferente e único!")
