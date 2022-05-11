import forca
import adivinhacao

def jogar():
    print("\n#################################")
    print("########Escolha seu jogo!########")
    print("#################################\n")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    jogar()