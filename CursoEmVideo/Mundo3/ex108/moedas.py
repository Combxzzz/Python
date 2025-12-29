def metade(arg, converte=False):
    res = arg / 2
    if converte:
        return converter(res)
    else:
        return res

def dobro(arg, converte=False):
    res = arg * 2
    if converte:
        return converter(res)
    else:
        return res

def aumentar(arg, porcent, converte=False):
    res = arg + (arg * porcent/100)
    if converte:
        return converter(res)
    else:
        return res

def diminuir(arg, porcent, converte=False):
    res = arg - (arg * porcent/100)
    if converte:
        return converter(res)
    else:
        return res

def converter(arg=0, moeda="RS"):
    return f"{moeda}{arg:.2f}".replace(".", ",")
