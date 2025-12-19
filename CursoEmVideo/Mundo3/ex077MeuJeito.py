palavras = ("PROGRAMACAO", "PYTHON", "GUANABARA", "ITALIA")
vogais = ("a", "e", "i", "o", "u")

for p in palavras:
    print(f"Na palavra {p.upper()} temos: ", end="")
    for letra in p:
        if letra.lower() in vogais:
            print(letra, end="")
    print()