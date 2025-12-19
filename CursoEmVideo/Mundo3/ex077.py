palavras = ("PROGRAMACAO", "PYTHON", "GUANABARA", "ITALIA")

for p in palavras:
    print(f"na palavra {p} temos: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end="")

