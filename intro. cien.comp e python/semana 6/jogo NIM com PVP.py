import random

def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    return computadorRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogadaValida = True

    return jogadorRemove


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')

def pvp():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    player1 = int(input('player 1 cara/coroa: [1/2]'))
    
    if player1 == 1:
        print('Player 2 ficou com coroa')
        player1 = 'cara'
        player2 = 'coroa'
    else:
        print('Player 2 ficou com cara')
        player1 = 'coroa'
        player2 = 'cara'
        
    resultado = random.randint(1,2)

    print("A moeda foi lançada")

    if resultado == 1:
        print('deu cara')
        if player1 == 'cara':
            print('player 1 começa')
            vezdoP1 = True
        else:
            print('player 2 começa')
            vezdoP1 = False
    if resultado == 2:
        print('Deu coroa')
        if player1 == 'coroa':
            print('player 1 começa')
            vezdoP1 = True
        else:
            print('Player 2 começa')
            vezdoP1 = False

    while n > 0:
        if vezdoP1:
            print('Vez do Player 1')
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('O Player 1 tirou uma peça')
            else:
                print()
                print('O Player 1 tirou', jogadorRemove, 'peças')
            if n == 0:
                ganhador = 'Player 1'

            vezdoP1 = False
        else:
            print('Vez do Player 2')
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Player 2 tirou uma peça')
            else:
                print()
                print('Player 2 tirou', jogadorRemove, 'peças')
            if n == 0:
                ganhador = 'Player 2'
            vezdoP1 = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print(f'Fim do jogo! O {ganhador} ganhou!')

def partida():
    n = int(input('Quantas peças? '))

    m = int(input('Limite de peças por jogada? '))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print('Voce começa!')

    else:
        print()
        print('Computador começa!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador tirou uma peça')
            else:
                print()
                print('O computador tirou', computadorRemove, 'peças')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', jogadorRemove, 'peças')
            vezDoPC = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato ')

tipoDePartida = int(input('3 - player vs player '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()

if tipoDePartida == 1:
    print()
    partida()

if tipoDePartida == 3:
    pvp()
