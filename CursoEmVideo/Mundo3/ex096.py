def area(lar, alt):
    a = lar * alt
    print(f"A area de um terreno {lar} x {alt} = {a}")

largura = float(input("Largura do terreno: "))
altura = float(input("Altura do terreno: "))

area(largura, altura)