import re
from random import randrange

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca !")
    print("*********************************")

    with open('palavras.txt', 'r') as arquivo:
        palavras = [p.strip() for p in arquivo]

    palavra_secreta = palavras[randrange(0, len(palavras))]
    palavra_secreta = palavra_secreta.upper()

    enforcou = False
    acertou = False

    chutes = ["_" for l in palavra_secreta]

    erros = 6

    while(not enforcou and not acertou):
        print("Você tem {} tentativas".format(erros))
        chute = input("Qual letra ? {} \n".format(' '.join([l.upper() for l in chutes])))
        chute = chute.strip().upper()

        index = 0
        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    chutes[index] = letra
                index += 1
        else:
            erros -= 1

        if ("_" not in chutes):
            print('Você ganhou !!!')
            print('Palavra "{}" completada !!'.format(palavra_secreta.upper()))
            break
        if (erros == 0):
            print('Enforcou !!!')
            break


    print("################### Fim do jogo! ####################")

if(__name__ == "__main__"):
    jogar()