from colorama import init, Fore, Style

init()

cores = {
    'titulo' : Fore.GREEN,
    'comando' : Fore.BLUE,
    'output' : Fore.MAGENTA,
    'fim' : Fore.RED,
    'limpar' : Style.RESET_ALL
}

def titulo(msg, cor=cores['titulo']):
    """

    :param msg: mensagem que deseja ser exibida
    :param cor: cor que deseja ser exibida com a mensagem
    :return: sem return
    """
    tam = len(msg) + 4
    print(cor + "-" * tam)
    print(f"{msg:^{tam}}")
    print("-" * tam + cores['limpar'] + "\n")


def pedir_ajuda(command, cor=cores['output']):
    """

    :param command: comanda para pedir ajuda
    :param cor: cor a ser exibida com a mensagem de ajuda
    :return: sem return
    """
    print("\n")
    titulo(f"Acessando ajuda do comando '{command}'", cor=cores['comando'])
    print(cor)
    help(command)
    print(cores['limpar'])


while True:
    titulo("SISTEMA DE AJUDA PyHELP")

    comando = input("Digite o nome do comando: ").lower().strip()
    if comando == "sair":
        break

    pedir_ajuda(comando)

print()
titulo("Volte sempre!", cor=cores['fim'])
