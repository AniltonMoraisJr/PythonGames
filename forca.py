def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca !")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    chutes = ["_" for l in palavra_secreta]

    while(not enforcou and not acertou):
        chute = input("Qual letra ? ({})".format(''.join(chutes)))
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                chutes[index] = letra
            index += 1
        if ("_" not in chutes):
            print('Palavra "{}" completada !!'.format(palavra_secreta))
            break

    print("################### Fim do jogo! ####################")

if(__name__ == "__main__"):
    jogar()