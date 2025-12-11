compras = float(input("Preco total das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

opcao = int(input("Escolha a opção de pagamento: "))

while True:
    if opcao == 1:
        total = compras - (compras * 0.10)
        print(f"Suas compras no final saem por R${total:.2f} com 10% de desconto.")

    elif opcao == 2:
        total = compras - (compras * 0.05)
        print(f"Suas compras no final saem por R${total:.2f} com 5% de desconto.")

    elif opcao == 3:
        total = compras
        parcelas = total / 2
        print(f"Suas compras serão parceladas em 2x de R${parcelas:.2f} sem juros. Total de R${total:.2f}.")

    elif opcao == 4:
        total = compras + (compras * 0.20)
        total_parcelas = int(input("Em quantas parcelas? "))
        parcelas = total / total_parcelas
        print(f"Suas compras serão parceladas em {total_parcelas}x de R${parcelas:.2f} com juros. Total de R${total:.2f}.")

    else:
        print("Opção inválida. Tente novamente.")
        opcao = int(input("Escolha a opção de pagamento: "))
        continue
    break
