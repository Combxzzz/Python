frutas = ("maça", "banana", "laranja", "uva")
if "banana" in frutas:
    print("banana esta na lista")

frutas = list(frutas)
frutas.append("abacaxi")
frutas = tuple(frutas)
print(frutas)