from random import randint

tabuleiro_jogador_1 = [['-' for a in range(8)] for b in range(8)]
tabuleiro_jogador_2 = [['-' for c in range(8)] for d in range(8)]
tabuleiro1 = [['-' for e in range(8)] for f in range(8)]
tabuleiro2 = [['-' for g in range(8)] for h in range(8)]


def exibe_tabuleiros(tabuleiro_a, tabuleiro_b, jogador_a, jogador_b):
    print('Mapa do jogador 1:', jogador_a, '\t\t\t\t\t\t\t', 'Mapa do jogador 2:', jogador_b)
    print(' ', end=' ')
    for i in range(8):
        print(i, end=' ')

    print('\t\t\t\t\t\t\t\t\t', end=' ')

    print(' ', end=' ')
    for i in range(8):
        print(i, end=' ')
    print()

    for linha in range(8):
        print(linha, end=' ')
        for coluna in range(8):
            print(tabuleiro_a[linha][coluna], end=' ')

        print('\t\t\t\t\t\t\t\t\t', end=' ')

        print(linha, end=' ')
        for coluna in range(8):
            print(tabuleiro_b[linha][coluna], end=' ')
        print()


def nomear_jogadores():
    op = 0
    jog1 = input('Entre com o seu nome: ')

    while jog1 == 'cpu':
        print('O nome do jogador 1 nao pode ser cpu')
        jog1 = input('Entre com o nome do jogador 1: ')

    while op != 1 and op != 2:
        print('1 - Jogar com outra pessoa')
        print('2 - Jogar com a maquina')
        op = int(input('Escolha uma opçao: '))

        if op != 1 and op != 2:
            print('Opçao invalida')

    if op == 1:
        jog2 = input('Entre com o nome do jogador 2: ')

        while jog1 == jog2:
            print('Os jogadores nao podem ter nomes iguais')
            jog2 = input('Entre com o nome do jogador 2: ')

        while jog2 == 'cpu':
            print('O nome do jogador 2 nao pode ser cpu')
            jog2 = input('Entre com o nome do jogador 2: ')

        return jog1, jog2
    else:
        return jog1, 'cpu'


def valida_coordenadas(linha, coluna):
    if linha < 0 or linha > 7 or coluna < 0 or coluna > 7:
        return False
    else:
        return True


# Verifica se e possivel posicionar um submarino nas coordenadas selecionadas
def aloca_submarino(linha, coluna, tabuleiro):
    if tabuleiro[linha][coluna] == '-':
        tabuleiro[linha][coluna] = 'S'
        return True
    else:
        return False


# Aloca submarinos com uma celula
def submarinos(jogador, tabuleiro):
    contador = 0
    print(jogador, ', posicione seus submarinos')

    while contador < 3:
        erro = True

        while erro:
            sub_lin = int(input('Entre com a linha do submarino %d[0 - 7]: ' % (contador + 1)))
            sub_col = int(input('Entre com a coluna do submarino %d[0 - 7]: ' % (contador + 1)))

            if valida_coordenadas(sub_lin, sub_col):
                if aloca_submarino(sub_lin, sub_col, tabuleiro):
                    contador += 1
                    erro = False
                else:
                    print('Posiçao ja ocupada')
            else:
                print('Coordenadas invalidas')


# Verifica se e possivel posicionar um cruzador nas coordenadas selecionadas
def aloca_cruzador(cruz_lin, cruz_col, tabuleiro):

    if tabuleiro[cruz_lin][cruz_col] == '-':
        if cruz_lin == 0:
            if cruz_col == 0:
                if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                    return True
                else:
                    return False
            elif cruz_col == 7:
                if tabuleiro[cruz_lin][cruz_col - 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                    return True
                else:
                    return False
            else:
                if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin][cruz_col - 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                    return True
                else:
                    return False
        elif cruz_lin == 7:
            if cruz_col == 0:
                if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                    return True
                else:
                    return False
            elif cruz_col == 7:
                if tabuleiro[cruz_lin][cruz_col - 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                    return True
                else:
                    return False
            else:
                if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin][cruz_col - 1] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                    return True
                elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                    tabuleiro[cruz_lin][cruz_col] = 'C'
                    tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                    return True
                else:
                    return False
        elif cruz_col == 0:
            if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                return True
            elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                return True
            elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                return True
            else:
                return False
        elif cruz_col == 7:
            if tabuleiro[cruz_lin][cruz_col - 1] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                return True
            elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                return True
            elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                return True
            else:
                return False
        else:
            if tabuleiro[cruz_lin][cruz_col + 1] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin][cruz_col + 1] = 'C'
                return True
            elif tabuleiro[cruz_lin][cruz_col - 1] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin][cruz_col - 1] = 'C'
                return True
            elif tabuleiro[cruz_lin + 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin + 1][cruz_col] = 'C'
                return True
            elif tabuleiro[cruz_lin - 1][cruz_col] == '-':
                tabuleiro[cruz_lin][cruz_col] = 'C'
                tabuleiro[cruz_lin - 1][cruz_col] = 'C'
                return True
            else:
                return False
    else:
        return False


# Aloca cruzadores com duas celulas
def cruzadores(jogador, tabuleiro):
    contador = 0
    print(jogador, ', posicione seus cruzadores')

    while contador < 3:
        erro = True

        while erro:
            cruz_lin = int(input('Entre com a linha do cruzador %d[0 - 7]: ' % (contador + 1)))
            cruz_col = int(input('Entre com a coluna do cruzador %d[0 - 7]: ' % (contador + 1)))

            if valida_coordenadas(cruz_lin, cruz_col):
                if aloca_cruzador(cruz_lin, cruz_col, tabuleiro):
                    contador += 1
                    erro = False
                else:
                    print('Nao e possivel posicionar um cruzador nessa posiçao. Essa posiçao ja esta ocupada ou nao ha'
                          ' celulas suficientes para alocar o navio em nenhuma direçao.')
            else:
                print('Coordenadas invalidas')


# Verifica se e possivel posicionar um porta avioes nas coordenadas selecionadas
def aloca_porta_avioes(pa_lin, pa_col, tabuleiro):

    if tabuleiro[pa_lin][pa_col] == '-':
        if pa_col < 3:
            if pa_lin < 3:
                if tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col + 1] == '-' and tabuleiro[pa_lin][pa_col + 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col + 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col + 1] = 'P'
                    tabuleiro[pa_lin][pa_col + 2] = 'P'
                    tabuleiro[pa_lin][pa_col + 3] = 'P'
                    return True
                else:
                    return False
            elif pa_lin > 4:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col + 1] == '-' and tabuleiro[pa_lin][pa_col + 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col + 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col + 1] = 'P'
                    tabuleiro[pa_lin][pa_col + 2] = 'P'
                    tabuleiro[pa_lin][pa_col + 3] = 'P'
                    return True
                else:
                    return False
            else:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col + 1] == '-' and tabuleiro[pa_lin][pa_col + 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col + 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col + 1] = 'P'
                    tabuleiro[pa_lin][pa_col + 2] = 'P'
                    tabuleiro[pa_lin][pa_col + 3] = 'P'
                    return True
                else:
                    return False
        elif pa_col > 4:
            if pa_lin < 3:
                if tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                else:
                    return False
            elif pa_lin > 4:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                else:
                    return False
            else:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                else:
                    return False
        else:
            if pa_lin < 3:
                if tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                elif tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                else:
                    return False
            elif pa_lin > 4:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col + 1] == '-' and tabuleiro[pa_lin][pa_col + 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col + 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col + 1] = 'P'
                    tabuleiro[pa_lin][pa_col + 2] = 'P'
                    tabuleiro[pa_lin][pa_col + 3] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                else:
                    return False
            else:
                if tabuleiro[pa_lin - 1][pa_col] == '-' and tabuleiro[pa_lin - 2][pa_col] == '-' and \
                        tabuleiro[pa_lin - 3][
                            pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin - 1][pa_col] = 'P'
                    tabuleiro[pa_lin - 2][pa_col] = 'P'
                    tabuleiro[pa_lin - 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin + 1][pa_col] == '-' and tabuleiro[pa_lin + 2][pa_col] == '-' and \
                        tabuleiro[pa_lin + 3][pa_col] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin + 1][pa_col] = 'P'
                    tabuleiro[pa_lin + 2][pa_col] = 'P'
                    tabuleiro[pa_lin + 3][pa_col] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col - 1] == '-' and tabuleiro[pa_lin][pa_col - 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col - 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col - 1] = 'P'
                    tabuleiro[pa_lin][pa_col - 2] = 'P'
                    tabuleiro[pa_lin][pa_col - 3] = 'P'
                    return True
                elif tabuleiro[pa_lin][pa_col + 1] == '-' and tabuleiro[pa_lin][pa_col + 2] == '-' and \
                        tabuleiro[pa_lin][
                            pa_col + 3] == '-':
                    tabuleiro[pa_lin][pa_col] = 'P'
                    tabuleiro[pa_lin][pa_col + 1] = 'P'
                    tabuleiro[pa_lin][pa_col + 2] = 'P'
                    tabuleiro[pa_lin][pa_col + 3] = 'P'
                    return True
                else:
                    return False
    else:
        return False


# Aloca porta avioes com quatro celulas
def porta_avioes(jogador, tabuleiro):
    contador = 0
    print(jogador, ', posicione seus porta avioes')

    while contador < 2:
        erro = True

        while erro:
            pa_lin = int(input('Entre com a linha do porta avioes %d[0 - 7]: ' % (contador + 1)))
            pa_col = int(input('Entre com a coluna do porta avioes %d[0 - 7]: ' % (contador + 1)))

            if valida_coordenadas(pa_lin, pa_col):
                if aloca_porta_avioes(pa_lin, pa_col, tabuleiro):
                    contador += 1
                    erro = False
                else:
                    print('Nao e possivel posicionar um porta avioes nessa posiçao. Essa posiçao ja esta ocupada ou nao'
                          ' ha celulas suficientes para alocar o navio em nenhuma direçao.')
            else:
                print('Coordenadas invalidas')


# Aloca submarinos aleatoriamente
def submarinos_aleatorios(tabuleiro):
    contador = 0

    while contador < 3:
        sub_lin = randint(0, 7)
        sub_col = randint(0, 7)

        if aloca_submarino(sub_lin, sub_col, tabuleiro):
            contador += 1


# Aloca cruzadores aleatoriamente
def cruzadores_aleatorios(tabuleiro):
    contador = 0

    while contador < 3:
        cruz_lin = randint(0, 7)
        cruz_col = randint(0, 7)

        if aloca_cruzador(cruz_lin, cruz_col, tabuleiro):
            contador += 1


# Aloca porta avioes aleatoriamente
def porta_avioes_aleatorios(tabuleiro):
    contador = 0

    while contador < 2:
        pa_lin = randint(0, 7)
        pa_col = randint(0, 7)

        if aloca_porta_avioes(pa_lin, pa_col, tabuleiro):
            contador += 1


def exibe_legendas():
    print('Legendas:')
    print("\t\t\t\t\t'-' - Posiçao ainda nao atingida")
    print("\t\t\t\t\t~ - Agua")
    print("\t\t\t\t\tS - Submarino")
    print("\t\t\t\t\tC - Cruzador")
    print("\t\t\t\t\tP - Porta Avioes")


# Valida as coordenadas de um tiro
def tiro(tabuleiro_alvo):
    erro = True
    linha = 0
    coluna = 0

    while erro:
        linha = int(input('Entre com a linha do Alvo: '))
        coluna = int(input('Entre com a coluna do Alvo: '))

        if not valida_coordenadas(linha, coluna):
            print('Coordenadas invalidas')
            continue

        if tabuleiro_alvo[linha][coluna] != '-':
            print('Voce ja escolheu essas coordenadas')
            continue

        erro = False
    else:
        return linha, coluna


# -------- O Codigo Principal Começa Aqui --------

rodada = 1
turno_jogador1 = True
turno_jogador2 = False
num_cels_jogador1 = num_cels_jogador2 = 17
vencedor = ''

jogador1, jogador2 = nomear_jogadores()

print(170 * '-',
      '\nBem vindos ao jogo Batalha Naval!\n'
      'O objetivo do jogo é afundar todos os navios do adversário. Para isso, cada jogador realiza na sua vez um dispar'
      'o selecionando as coordenadas no teclado.\nSe é possível alcançar um navio inimigo, joga-se outra vez.\n',
      'Os navios disponiveis sao:\n',
      '3 Submarinos de 1 celula cada\n',
      '3 cruzadores de 2 celulas cada\n',
      '2 porta avioes de 4 celulas cada\n',
      170 * '-')

print(15 * '-', jogador1, 15 * '-')
submarinos(jogador1, tabuleiro_jogador_1)
cruzadores(jogador1, tabuleiro_jogador_1)
porta_avioes(jogador1, tabuleiro_jogador_1)

if jogador2 == 'cpu':
    submarinos_aleatorios(tabuleiro_jogador_2)
    cruzadores_aleatorios(tabuleiro_jogador_2)
    porta_avioes_aleatorios(tabuleiro_jogador_2)
else:
    print(15 * '-', jogador2, 15 * '-')
    submarinos(jogador2, tabuleiro_jogador_2)
    cruzadores(jogador2, tabuleiro_jogador_2)
    porta_avioes(jogador2, tabuleiro_jogador_2)

'''
Mostra os tabuleiros para conferencia

exibe_tabuleiros(tabuleiro_jogador_1, tabuleiro_jogador_2, jogador1, jogador2)
'''

while vencedor == '':

    while turno_jogador1:
        print(5 * '-', 'Rodada:', rodada, 5 * '-')
        print('Turno do jogador 1:', jogador1, '\n')

        exibe_tabuleiros(tabuleiro1, tabuleiro2, jogador1, jogador2)

        tiro_lin, tiro_col = tiro(tabuleiro2)

        if tabuleiro_jogador_2[tiro_lin][tiro_col] == 'S':
            print(jogador1, 'acertou um submarino!')

            tabuleiro2[tiro_lin][tiro_col] = 'S'
            num_cels_jogador2 -= 1

            if num_cels_jogador2 == 0:
                vencedor = jogador1
                break
            else:
                rodada += 1
        elif tabuleiro_jogador_2[tiro_lin][tiro_col] == 'C':
            print(jogador1, 'acertou um cruzador!')

            tabuleiro2[tiro_lin][tiro_col] = 'C'
            num_cels_jogador2 -= 1

            if num_cels_jogador2 == 0:
                vencedor = jogador1
                break
            else:
                rodada += 1
        elif tabuleiro_jogador_2[tiro_lin][tiro_col] == 'P':
            print(jogador1, 'acertou um porta avioes!')

            tabuleiro2[tiro_lin][tiro_col] = 'P'
            num_cels_jogador2 -= 1

            if num_cels_jogador2 == 0:
                vencedor = jogador1
                break
            else:
                rodada += 1
        else:
            print(jogador1, ' errou os navios. O tiro foi para a agua!')
            tabuleiro2[tiro_lin][tiro_col] = '~'
            turno_jogador1 = False
            turno_jogador2 = True

    while turno_jogador2:
        print(5 * '-', 'Rodada:', rodada, 5 * '-')
        print('Turno do jogador 2:', jogador2, '\n')

        exibe_legendas()

        exibe_tabuleiros(tabuleiro1, tabuleiro2, jogador1, jogador2)

        if jogador2 == 'cpu':
            tiro_lin = randint(0, 7)
            tiro_col = randint(0, 7)

            while tabuleiro1[tiro_lin][tiro_col] != '-':
                tiro_lin = randint(0, 7)
                tiro_col = randint(0, 7)
        else:
            tiro_lin, tiro_col = tiro(tabuleiro1)

        if tabuleiro_jogador_1[tiro_lin][tiro_col] == 'S':
            print(jogador2, 'acertou um submarino!')

            tabuleiro1[tiro_lin][tiro_col] = 'S'
            num_cels_jogador1 -= 1

            if num_cels_jogador1 == 0:
                turno_jogador1 = False
                vencedor = jogador2
                break
            else:
                rodada += 1
        elif tabuleiro_jogador_1[tiro_lin][tiro_col] == 'C':
            print(jogador2, 'acertou um cruzador!')

            tabuleiro1[tiro_lin][tiro_col] = 'C'
            num_cels_jogador1 -= 1

            if num_cels_jogador1 == 0:
                turno_jogador1 = False
                vencedor = jogador2
                break
            else:
                rodada += 1
        elif tabuleiro_jogador_1[tiro_lin][tiro_col] == 'P':
            print(jogador2, 'acertou um porta avioes!')

            tabuleiro1[tiro_lin][tiro_col] = 'P'
            num_cels_jogador1 -= 1

            if num_cels_jogador1 == 0:
                turno_jogador1 = False
                vencedor = jogador2
                break
            else:
                rodada += 1
        else:
            print(jogador2, ' errou os navios. O tiro foi para a agua!')
            tabuleiro1[tiro_lin][tiro_col] = '~'
            rodada += 1
            turno_jogador2 = False
            turno_jogador1 = True

print(170 * '-')
print('Fim de jogo na rodada:', rodada)
print('Tabuleiros Iniciais:')
exibe_tabuleiros(tabuleiro_jogador_1, tabuleiro_jogador_2, jogador1, jogador2)
print('VENCEDOR:', vencedor, '!!!')
