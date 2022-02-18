import re
from random import randrange

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca !")
    print("*********************************")

    palavra_secreta = carrega_palavra_secreta()

    enforcou = False
    acertou = False

    chutes = ["_" for l in palavra_secreta]

    erros = 7

    while(not enforcou and not acertou):
        print("Você tem {} tentativas".format(erros))
        chute = input("Qual letra ? {} \n".format(' '.join([l.upper() for l in chutes])))
        chute = chute.strip().upper()


        if (chute in palavra_secreta):
            chutes = grava_chutes(chute, chutes, palavra_secreta)
        else:
            erros -= 1
            desenha_forca(erros)

        if ("_" not in chutes):
            imprime_mensagem_vencedor(palavra_secreta = palavra_secreta)
            break
        if (erros == 0):
            imprime_mensagem_perdedor(palavra_secreta)
            break


    print("################### Fim do jogo! ####################")

###### Métodos auxiliares #########

def carrega_palavra_secreta():
    with open('palavras.txt', 'r') as arquivo:
        palavras = [p.strip() for p in arquivo]

    palavra_secreta = palavras[randrange(0, len(palavras))]
    palavra_secreta = palavra_secreta.upper()
    return palavra_secreta

def grava_chutes(chute, chutes, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            chutes[index] = chute
        index += 1
    return chutes

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("A palavra era {}".format(palavra_secreta))
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

if(__name__ == "__main__"):
    jogar()