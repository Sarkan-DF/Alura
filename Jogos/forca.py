import random

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    chances = 6

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas, chances)
        else:
            erros += 1
            desenha_forca(erros)
            chances = chances - 1
            print("Você errou ainda tem {} chances.\n".format(chances))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_abertura():
    print("\n#################################")
    print("Bem vindo ao jogo de Forca!")
    print("#################################\n")

def carrega_palavra_secreta():
    categoria_palavra = False

    while(categoria_palavra != "F" and categoria_palavra != "C" and categoria_palavra != "N"):
        categoria_palavra = input("\nQual categoria gostaria de escolher? \n"
                                  "Digite 'F' para Frutas, 'C' para Carros ou 'N' para Nomes: ")
        categoria_palavra = categoria_palavra.upper().strip()

    if(categoria_palavra == "F"):
        print("Voçe escolheu a categoria:")
        print("####### FRUTAS ###########")
        arquivo = open('frutas.txt', 'r')
        palavras = []

    elif(categoria_palavra == "C"):
        print("Voçe escolheu a categoria:")
        print("####### CARROS ###########")
        arquivo = open('carros.txt', 'r')
        palavras = []

    elif (categoria_palavra == "N"):
        print("Voçe escolheu a categoria:")
        print("######## NOMES ###########")
        arquivo = open('nomes.txt', 'r')
        palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializar_letras_acertadas(palavra):
    print("\n")
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas, chances):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            letras_faltando = str(letras_acertadas.count('_'))
        index = index + 1
    print('Acertou mas ainda faltam acertar {} letras'.format(letras_faltando))
    print("E ainda tem {} chances.\n".format(chances))

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()