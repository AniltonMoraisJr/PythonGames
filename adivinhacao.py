import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    total_de_tentativas = 3
    # the function random return values between 0.0 and 1.0. The function randrange return values between the parameters
    numero_secreto = round(random.randrange(0, 101))
    pontos = 1000

    print("Digite o nível de dificuldade do jogo")
    print("1 - Facil, 2 - Médio, 3 - Dificil")
    dificuldade = int(input())

    if(dificuldade == 1):
        total_de_tentativas = 20
    elif(dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Rodada {} de {} tentativas".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu chute entre 1 e 100: ")
        print("Você digitou: ", chute_str)

        chute_int = int(chute_str)

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if(chute_int < 1 or chute_int > 100):
            print("Digite um valor entre 1 e 100 !")
            continue

        if(acertou):
            imprime_mensagem_vencedor(numero_secreto, pontos)
            break
        else:
            if (maior):
                print("O chute foi maior")
            elif(menor):
                print("O chute foi menor !")

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

        if (rodada < total_de_tentativas):
            print("--------------------------------------------------")
        if (rodada == total_de_tentativas):
            imprime_mensagem_perdedor(numero_secreto, pontos)
    print("################### Fim do jogo! ####################")

def imprime_mensagem_vencedor(numero_secreto, pontos):
    print("Parabéns, você ganhou!")
    print("A numero secreto era {} !! Você fez {} pontos.".format(numero_secreto, pontos))
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

def imprime_mensagem_perdedor(numero_secreto, pontos):
    print("Puxa, você perdeu =/ !")
    print("A numero secreto era {} !! Você fez {} pontos.".format(numero_secreto, pontos))
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

if(__name__ == "__main__"):
    jogar()