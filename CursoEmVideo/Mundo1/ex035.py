print("Analizador de triângulos")
a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR um triângulo", end=' ')

    if a == b == c:
        print("EQUILÁTERO!")
    elif a != b and b != c and a != c:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")

#Tentei fazer de outra forma, não sei se está certo