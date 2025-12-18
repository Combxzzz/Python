times = (
    "Flamengo",
    "Palmeiras",
    "Cruzeiro",
    "Mirassol",
    "Fluminense",
    "Botafogo",
    "Bahia",
    "São Paulo",
    "Grêmio",
    "Bragantino",
    "Atlético-MG",
    "Santos",
    "Corinthians",
    "Vasco",
    "Vitória",
    "Internacional",
    "Ceará",
    "Fortaleza",
    "Juventude",
    "Sport"
)

print(f"Times: {times}")

print(f"Os primeiros 5 colocados são: {times[:5]}")
print(f"Os ultimos 4 colocados são: {times[-4:]}")
print(f"Times em ordem alfabetica: {sorted(times)}\n")
# Vo substituir a Chapecoense pelo São Paulo
# com enumerate
print("Com enumarate:")
for posi, time in enumerate(times):
    if time == "São Paulo":
        print(f"{time} esta na posição {posi + 1} na tabela\n")

# com index
print("Com index: ")
print(f"São Paulo enta na posicao {times.index("São Paulo") + 1} na tabela")
