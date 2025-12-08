user = int(input("Digite a base do triangulo: "))
estrelas = []

def piramide(base):
    l = 2 * base - 1
    for i in range(1, base + 1):
        stars = ("*" * (2*i - 1))
        print(stars.center(l))
        estrelas.append(len(stars))


piramide(user)
print(estrelas)



# def piramide(base):
#     for i in range(1, base + 1):
#         print("*" * i)


# piramide(5)