import random

def jogar():
    print("\n#################################")
    print("Bem vindo ao jogo de adivinhação!")
    print("#################################\n")

    total_de_tentativas = 0
    numero_secreto = random.randrange(0, 101)
    pontos = 1000

    print("Qual nivel de dificuldade você quer?")
    nivel = int(input("(1)Facil, (2)Medio ou (3)Dificio: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}." .format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou o numero:", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = (chute == numero_secreto)
        maior   = (chute  > numero_secreto)
        menor   = (chute  < numero_secreto)

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou, Chutou alto!\n")
                if(rodada == total_de_tentativas):
                    print("O numero secreto era {} e a sua pontoação foi {}!".format(numero_secreto,pontos))
            elif(menor):
                print("Você errou, Chutou baixo!\n")
                if (rodada == total_de_tentativas):
                    print("O numero secreto era {} e a sua pontoação foi {}!".format(numero_secreto, pontos))

    print("\nFim de jogo!")

if(__name__ == "__main__"):
    jogar()