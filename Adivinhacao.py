import random



def jogar():

    
    # imprime_mensagem_abertura()

    numero_secreto=(random.randrange(1,101)) 
    TotT=0
    pontos=1000

    print('Qual nivel de dificuldade?',numero_secreto)#deixei a resposta pra facilitar quando jogar, mas qql coisa só tirar a variavel
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if(nivel==1):
        TotT=20
    elif(nivel==2):
        TotT=10
    else:
        TotT=5

    for rodada in range(1,TotT+1):
        print("tentativa {} de {} ".format(rodada,TotT))
        chute_str= input('Digite um numero entre 1 e 100: ')
        print("Voce digitou",chute_str)
        chute=int(chute_str)

        if(chute<1 or chute>100):
            print('Voce deve digitar um numero entre 1 e 100!')
            continue
        acertou=chute==numero_secreto
        maior  = chute>numero_secreto
        menor  = chute<numero_secreto
        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos=abs(numero_secreto-chute)
            pontos=pontos-pontos_perdidos
    print('Fim de jogo!')

if(__name__=='__main__'):
    jogar()



def imprime_mensagem_abertura():
    print('********************************')
    print('******Jogo da Adivinhação!******')
    print('********************************')
