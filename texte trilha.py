##Jogo da Trilha
##Instituto Federal Catarinense - Campus Concórdia
##Trabalho de Programação - Professor tiago.mazzutti
##Cria por: guilherme B. de Almeida 
##matricula: 2019303606
print('''
_________________________________________________________________________________
                 POSIÇÕES                                                        |
\u24ea----------\u2460----------\u2461                                                        |
|           |           |                                                        |
|   \u2462------\u2463------\u2463   |                                                        |
|   |       |       |   |                                                        |
|   |   \u2464--\u2465--\u2466   |   |                  JOGO DA TRILHA                        |
|   |   |       |   |   |                                                        |
\u2467--\u2468--\u2469       \u246a--\u246b--\u246c                                                        |
|   |   |       |   |   |                                                        |
|   |   \u246d--\u246e--\u246f   |   |                 programação                            |
|   |       |       |   |                                                        |
|   \u2470------\u2471------\u2472   |                                                        |
|           |           |                                                        |
\u2473----------\u3251----------\u3252                                                        |
                         Desenvolvido por Guilherme B. de Almeida e Helenton     |
_________________________________________________________________________________| ''')

esecutar = str(input("desija esecutar o jogo. se quiser esecutar o jogo digite 'S', se não deseja esecutar digite 'N':"))
def confirir_jogad_1(casas):
    if casas[0] == casas[1] == casas[2] == '\u26ab' or\
       casas[2] == casas[14] == casas[23] == '\u26ab' or\
       casas[23] == casas[14] == casas[2] == '\u26ab' or\
       casas[5] == casas[13] == casas[20] == '\u26ab' or\
       casas[20] == casas[13] == casas[5] == '\u26ab' or\
       casas[8] == casas[12] == casas[17] == '\u26ab' or\
       casas[17] == casas[12] == casas[8] == '\u26ab' or\
       casas[1] == casas[4] == casas[7] == '\u26ab' or\
       casas[7] == casas[4] == casas[1] == '\u26ab' or\
       casas[16] == casas[19] == casas[22] == '\u26ab' or\
       casas[22] == casas[19] == casas[16] == '\u26ab' or\
       casas[6] == casas[11] == casas[15] == '\u26ab' or\
       casas[15] == casas[11] == casas[6] == '\u26ab' or\
       casas[3] == casas[10] == casas[18] == '\u26ab' or\
       casas[18] == casas[10] == casas[3] == '\u26ab' or\
       casas[0] == casas[9] == casas[21] == '\u26ab' or\
       casas[21] == casas[9] == casas[0] == '\u26ab' or\
       casas[3] == casas[4] == casas[5] == '\u26ab' or\
       casas[6] == casas[7] == casas[8] == '\u26ab' or\
       casas[9] == casas[10] == casas[11] == '\u26ab' or\
       casas[12] == casas[13] == casas[14] == '\u26ab' or\
       casas[15] == casas[16] == casas[17] == '\u26ab' or\
       casas[18] == casas[19] == casas[20] == '\u26ab' or\
       casas[21] == casas[22] == casas[23] == '\u26ab':
       print("voce pode tirar uma peca, jogador %s " % p)
       tira1 = int(input('digite o numero da peca que vc deseja tirar ---> '))
       if casas[tira1] == '/u26ab' or casas[tira1] == '-':
           print('Valor invalido!!!')
       else:
           casas[tira1] = '-'          
def confirir_jogad_2(casas):
    if casas[0] == casas[1] == casas[2] == '\u26aa' or\
        casas[2] == casas[14] == casas[23] == '\u26aa' or\
        casas[23] == casas[14] == casas[2] == '\u26aa' or\
        casas[5] == casas[13] == casas[20] == '\u26aa' or\
        casas[20] == casas[13] == casas[5] == '\u26aa' or\
        casas[8] == casas[12] == casas[17] == '\u26aa' or\
        casas[17] == casas[12] == casas[8] == '\u26aa' or\
        casas[1] == casas[4] == casas[7] == '\u26aa' or\
        casas[7] == casas[4] == casas[1] == '\u26aa' or\
        casas[16] == casas[19] == casas[22] == '\u26aa' or\
        casas[22] == casas[19] == casas[16] == '\u26aa' or\
        casas[6] == casas[11] == casas[15] == '\u26aa' or\
        casas[15] == casas[11] == casas[6] == '\u26aa' or\
        casas[3] == casas[10] == casas[18] == '\u26aa' or\
        casas[18] == casas[10] == casas[3] == '\u26aa' or\
        casas[0] == casas[9] == casas[21] == '\u26aa' or\
        casas[21] == casas[9] == casas[0] == '\u26aa' or\
        casas[3] == casas[4] == casas[5] == '\u26aa' or\
        casas[6] == casas[7] == casas[8] == '\u26aa' or\
        casas[9] == casas[10] == casas[11] == '\u26aa' or\
        casas[12] == casas[13] == casas[14] == '\u26aa' or\
        casas[15] == casas[16] == casas[17] == '\u26aa' or\
        casas[18] == casas[19] == casas[20] == '\u26aa' or\
        casas[21] == casas[22] == casas[23] == '\u26aa':
        print("voce pode tirar uma peca, jogador %s" % b) 
        tira2 = int(input('digite o numero da peca que vc deseja tirar ---> '))
        if casas[tira2] == '/u26aa' or casas[tira2] == '-':
            casas[tira2] = '-' 
            print('Valor invalido!!!')
        else:
            casas[tira2] = '-'
def tabuleiro(casas):
    print('')
    print('\t %s-----------%s-----------%s' % (casas[0], casas[1], casas[2]))
    print('\t |           |           |')
    print('\t |   %s-------%s-------%s   |' % (casas[3], casas[4], casas[5]))
    print('\t |   |       |       |   |')
    print('\t |   |   %s---%s---%s   |   |' % (casas[6], casas[7], casas[8]))
    print('\t |   |   |       |   |   |')
    print('\t %s---%s---%s       %s---%s---%s' % (casas[9], casas[10], casas[11], casas[12], casas[13], casas[14]))
    print('\t |   |   |       |   |   |')
    print('\t |   |   %s---%s---%s   |   |' % (casas[15], casas[16], casas[17]))
    print('\t |   |       |       |   |')
    print('\t |   %s-------%s-------%s   |' % (casas[18], casas[19], casas[20]))
    print('\t |           |           |')
    print('\t %s----------%s-----------%s' % (casas[21], casas[22], casas[23]))
    print('')


casas = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', '-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
##---------------------------------------------------------definir casa------------------------------------------------------
linha = 0
if esecutar == 'S':
    p = input('Digite seu nome primeiro jogador !!! ---> ')
    b = input('Digite seu nome segundo jogador !!! ---> ')
else:
    exit()
x = 1
while x <= 9:
    #while x <= 9:
   # p = input('Digite seu nome primeiro jogador !!! ---> ')
    #b = input('Digite seu nome segundo jogador !!! ---> ')

    ## distribui casa do jogador 1
    print('')
    print("\u24ea----------\u2460----------\u2461 ")
    print("|           |           |        |      ")
    print("|   \u2462------\u2463------\u2464   | ")
    print("|   |       |       |   |               ")
    print("|   |   \u2465--\u2466--\u2467   |   |  ")
    print("|   |   |       |   |   |                 ")
    print("\u2468--\u2469--\u246a       \u246b--\u246c--\u246d   ")
    print("|   |   |       |   |   |                  ")
    print("|   |   \u246e--\u246f--\u2470   |   |   ")
    print("|   |       |       |   |              ")
    print("|   \u2471------\u2472------\u2473   |  ")
    print("|           |           |               ")
    print("\u2451----------\u3252----------\u3253  ")
    print('')
    linha = int(input(" %s, Faça sua jogada ->>" % p))
    if linha < 0 or linha > 23:
        print('Valor invalido!!!')
        exit()
    elif casas[linha] != '-':
        print('Voce não pode jogar nessa posiçao!!!, perdeu a vez.')
    else:
        casas[linha] = '\u26ab'

        print('')
        print("\u24ea----------\u2460----------\u2461 ")
        print("|           |           |        |      ")
        print("|   \u2462------\u2463------\u2464   | ")
        print("|   |       |       |   |               ")
        print("|   |   \u2465--\u2466--\u2467   |   |  ")
        print("|   |   |       |   |   |                 ")
        print("\u2468--\u2469--\u246a       \u246b--\u246c--\u246d   ")
        print("|   |   |       |   |   |                  ")
        print("|   |   \u246e--\u246f--\u2470   |   |   ")
        print("|   |       |       |   |              ")
        print("|   \u2471------\u2472------\u2473   |  ")
        print("|           |           |               ")
        print("\u2451----------\u3252----------\u3253  ")
        print('')

        tabuleiro(casas)
        confirir_jogad_1(casas)
##jogador 2
        linha = int(input(" %s, Faça sua jogada -->>" % b))
        if linha < 0 or linha > 23:
            print('Valor invalido!!!.')
            exit()
        elif casas[linha] != '-':
            print('Voce nao pode jogar nessa posiçao!!!, perdeu a vez.')
        else:
            casas[linha] = '\u26aa'

            print('')
            print("\u24ea----------\u2460----------\u2461 ")
            print("|           |           |        |      ")
            print("|   \u2462------\u2463------\u2464   | ")
            print("|   |       |       |   |               ")
            print("|   |   \u2465--\u2466--\u2467   |   |  ")
            print("|   |   |       |   |   |                 ")
            print("\u2468--\u2469--\u246a       \u246b--\u246c--\u246d   ")
            print("|   |   |       |   |   |                  ")
            print("|   |   \u246e--\u246f--\u2470   |   |   ")
            print("|   |       |       |   |              ")
            print("|   \u2471------\u2472------\u2473   |  ")
            print("|           |           |               ")
            print("\u2451----------\u3252----------\u3253  ")
            print('')
            
            tabuleiro(casas)
            confirir_jogad_2(casas)        
    x = x + 1
## ------------------------------- movimentação das pessas-----------------------------------------------
    ##jogador1
x2 = 0
while x2 < 1000:
    ###para o jogador p
    troca1 = int(input('jogador %s digite a peça que vc deseja mover-->>' % p))
    ganhador1 = str(tabuleiro(casas)).count('\u26ab')
    if ganhador1 == 2:
            print('%s voce ganhou parabens !!!!' % p)
            exit()

    if casas[troca1] == '\u26ab':
        troca1 = int(input('%s digite em que posisao voçe quer movela, lembramdo que voçe so pode jogar somente na linha e tambem vc nao pode pular mais de uma casa.' % p))
    elif casas[troca1] == '-' and casas[troca1] != '\u26aa':
        casas[troca1] = '\u26ab'
        casas[troca1] = '-'
        tabuleiro(casas)
        confirir_jogad_1(casas)
    else:
        print('jogada invalida jogue novamente. -->>')
        troca1 = int(input('digite em que posisao voçe quer movela, lembramdo que voçe so pode jogar somente na linha e tambem vc nao pode pular mais de uma casa.'))
        casas[troca1] = '\u26ab'
        casas[troca1] = '-'
        confirir_jogad_1(casas)
        tabuleiro(casas)
    print('----------------------------------------------------------------------')
    troca = int(input('jogador %s digite a peça que vc deseja mover. >>>' % p))
    ganhador2 = str(tabuleiro(casas)).count('\u26aa')
    if ganhador2 == 2:
                print('%s voce ganhou parabens !!!!.' % b)
                exit()
    troca2 = int(input('jogador %s digite a peça que vc deseja mover. ->>>>' % b))
    if casas[troca2] == '\u26aa':
            troca3 = input('%s digite em que posisao voçe quer movela, lembramdo que voçe so pode jogar somente na linha e tambem vc nao pode pular mais de uma casa.')
    elif casas[troca3] == '-' and casas[troca3] != '\u26ab':
            casas[troca3] = '\u26aa'
            casas[troca2] = '-'
            tabuleiro(casas)
            confirir_jogad_2(casas)
    else:
        print('jogada invalida jogue novamente.-->>')
        troca1 = int(input('digite em que posisao voçe quer movela, lembramdo que voçe so pode jogar somente na linha e tambem vc nao pode pular mais de uma casa.'))
        casas[troca3] = '\u26aa'
        casas[troca2] = '-'
        confirir_jogad_2(casas)
        tabuleiro(casas)
x = x - 1
