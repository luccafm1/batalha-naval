# esqueleto básico
# integrar PC
# consertar erro out of bounds

import random

tabuleiro = [[0] * 10 for _ in range(5)]
tabuleiro2 = [[0] * 10 for _ in range(5)]

tabuleiroPLAYER = [['~'] * 10 for _ in range(5)]
tabuleiroPC = [['~'] * 10 for _ in range(5)]

embarcacao_player = 0
embarcacao_pc = 0

vida_embarcacoes = {'AV': 5, 'NT': 4, 'CT': 3, 'SB': 2, 'DT': 1}
vida_embarcacoesPC = {'AV': 5, 'NT': 4, 'CT': 3, 'SB': 2, 'DT': 1}


def mostrar_tabuleiro(jogador, visivel):
    if jogador == 'PC':
        print("  Tabuleiro do Computador")
        print()
        print("   0 1 2 3 4 5 6 7 8 9")
        for i, coluna in enumerate(tabuleiro if visivel else tabuleiro):
            print(f"{i + 0:2d} ", end='')
            for c in coluna:
                print(c, end=' ')
            print()
        print()
    else:
        print("  Tabuleiro do Jogador")
        print()
        print("   0 1 2 3 4 5 6 7 8 9")
        for i, row in enumerate(tabuleiroPLAYER if visivel else tabuleiro2):
            print(f"{i + 0:2d} ", end='')
            for c in row:
                print(c, end=' ')
            print()
        print()


def checar_embarcacoes(jogador):

    if jogador == 'PLAYER':
        if vida_embarcacoes['AV'] == 0:
            print('Porta-Aviões aliado afundado!')
            vida_embarcacoes.pop('AV')
        elif vida_embarcacoes['NT'] == 0:
            print('Navio-Tanque aliado afundado!')
            vida_embarcacoes.pop('NT')
        elif vida_embarcacoes['CT'] == 0:
            print('Contra-Torpedeiro aliado afundado!')
            vida_embarcacoes.pop('CT')
        elif vida_embarcacoes['SB'] == 0:
            print('Submarino aliado afundado!')
            vida_embarcacoes.pop('SB')
        elif vida_embarcacoes['DT'] == 0:
            print('Destroier aliado afundado!')
            vida_embarcacoes.pop('DT')
    else:
        if vida_embarcacoesPC['AV'] == 0:
            print('Porta-Aviões inimigo afundado!')
            vida_embarcacoesPC.pop('AV')
        elif vida_embarcacoesPC['NT'] == 0:
            print('Navio-Tanque inimigo afundado!')
            vida_embarcacoesPC.pop('NT')
        elif vida_embarcacoesPC['CT'] == 0:
            print('Contra-Torpedeiro inimigo afundado!')
            vida_embarcacoesPC.pop('CT')
        elif vida_embarcacoesPC['SB'] == 0:
            print('Submarino inimigo afundado!')
            vida_embarcacoesPC.pop('SB')
        elif vida_embarcacoesPC['DT'] == 0:
            print('Destroier inimigo afundado!')
            vida_embarcacoesPC.pop('DT')


def jogada(linha, coluna):
    while True:
        if jogador == 'PC':
            if tabuleiro2[linha][coluna] == 0:
                tabuleiroPLAYER[linha][coluna] = 'O'
                return False
            else:
                if tabuleiro2[linha][coluna] == 5:
                    vida_embarcacoes['AV'] -= 1
                    checar_embarcacoes('PLAYER')
                elif tabuleiro2[linha][coluna] == 4:
                    vida_embarcacoes['NT'] -= 1
                    checar_embarcacoes('PLAYER')
                elif tabuleiro2[linha][coluna] == 3:
                    vida_embarcacoes['CT'] -= 1
                    checar_embarcacoes('PLAYER')
                elif tabuleiro2[linha][coluna] == 2:
                    vida_embarcacoes['SB'] -= 1
                    checar_embarcacoes('PLAYER')
                elif tabuleiro2[linha][coluna] == 1:
                    vida_embarcacoes['DT'] -= 1
                    checar_embarcacoes('PLAYER')

                tabuleiroPLAYER[linha][coluna] = 'X'
                return True
        else:
            try:
                if tabuleiro[linha][coluna] == 0:
                    tabuleiroPC[linha][coluna] = 'O'
                    return False
                else:
                    tabuleiroPC[linha][coluna] = 'X'
                    return True
            except IndexError:
                print(f'ERRO: Posição inválida {linha, coluna}. Impossível posicionar um veículo fora do jogo! '
                      f'Tente novamente.')
                pass


def embarcacoes(linha, coluna, embarcacao, orientacao, jogador):
    tamanho = 0

    if embarcacao == 'AV':
        tamanho_limite = 5
        valor_embarcacao = 5
    elif embarcacao == 'NT':
        tamanho_limite = 4
        valor_embarcacao = 4
    elif embarcacao == 'CT':
        tamanho_limite = 3
        valor_embarcacao = 3
    elif embarcacao == 'SB':
        tamanho_limite = 2
        valor_embarcacao = 2
    elif embarcacao == 'DT':
        tamanho_limite = 1
        valor_embarcacao = 1
    else:
        print('ERRO: Veículo inválido!')
        return False
    if orientacao == 'h':
        start_position = (linha, coluna)
        end_position = (linha, coluna + tamanho_limite)
    else:
        start_position = (linha, coluna)
        end_position = (linha + tamanho_limite, coluna)

    start_row, start_col = start_position
    end_row, end_col = end_position

    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if tabuleiro2[i][j] != 0:
                print('ERRO: Veículo sobreposto!')
                return False

    while tamanho < tamanho_limite:
        if jogador == 'PLAYER':
            if orientacao == 'h':
                if coluna + tamanho_limite >= 12:
                    print('ERRO: Posição inválida. O veículo não pode ficar fora do tabuleiro!')
                    return False
                tabuleiro2[linha][coluna + tamanho] = valor_embarcacao
                tamanho += 1

            elif orientacao == 'v':
                if linha + tamanho_limite >= 7:
                    print('ERRO: Posição inválida. O veículo não pode ficar fora do tabuleiro!')
                    return False
                tabuleiro2[linha + tamanho][coluna] = valor_embarcacao
                tamanho += 1
                return True
            else:
                orientacao = input('ERRO: Entrada incorreta. Escolha orientação horizontal ou vertical (h/v) '
                                   'do posicionamento: ')
                continue
        else:
            if orientacao == 'h':
                if coluna + tamanho_limite >= 10:
                    return False
                elif tabuleiro2[linha][coluna + tamanho] != 0:
                    while tamanho != -1:
                        tamanho -= 1
                        tabuleiro2[linha][coluna - tamanho] = 0
                    return False
                tabuleiro2[linha][coluna + tamanho] = valor_embarcacao
                tamanho += 1
            elif orientacao == 'v':
                if linha + tamanho_limite >= 5:
                    return False
                elif tabuleiro2[linha + tamanho][coluna] != 0:
                    while tamanho != -1:
                        tamanho -= 1
                        tabuleiro2[linha - tamanho][coluna] = 0
                    return False
                tabuleiro2[linha + tamanho][coluna] = valor_embarcacao
                tamanho += 1

    return True


def inicializar():

    total_embarcacoes = ['']
    tipos_embarcacoes = ['AV', 'NT', 'CT', 'SB', 'DT']

    embarcacoes_total = 0
    embarcacoes_totalPC = 0
    while embarcacoes_total < 5:
        mostrar_tabuleiro('PLAYER', False)
        embarcacao = input(
            'Digite o veículo (AV: Porta-Avião / NT: Navio-Tanque / CT: Contra-Torpedeiro '
            '/ SB: Submarino / DT: Destroier): '
        )
        if embarcacao not in tipos_embarcacoes:
            print('ERRO: Veículo inválido.')
            continue
        if embarcacao in total_embarcacoes:
            print('ERRO: Apenas selecione um de cada tipo.')
            continue
        print(f'{embarcacao} selecionado!')

        linha = int(input('Digite a linha para posicionar seu veículo: '))
        coluna = int(input('Digite a coluna para posicionar seu veículo: '))

        orientacao = input('Escolha orientação horizontal ou vertical (h/v) do posicionamento: ')

        try:
            if embarcacoes(linha, coluna, embarcacao, orientacao, 'PLAYER'):
                embarcacoes_total += 1
            else:
                continue

        except IndexError:
            print(f'ERRO: Posição inválida {linha, coluna}. Impossível posicionar um veículo fora do jogo! '
                  f'Tente novamente.')
            continue
        print(f'Posicionado {embarcacao} em {linha, coluna}')

        total_embarcacoes.append(embarcacao)

    while embarcacoes_totalPC != 5:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)
        orientacao = random.choice(['h,' 'v'])
        embarcacao = random.choice(tipos_embarcacoes)

        if embarcacoes(linha, coluna, embarcacao, orientacao, 'PC'):
            embarcacoes_totalPC += 1
        else:
            continue


def visual():

    print('')
    print('')
    mostrar_tabuleiro('PC', True)
    print('')
    print(f'Embarcações restantes: {embarcacao_pc}')
    print('')
    mostrar_tabuleiro('PLAYER', True)
    print('')
    print(f'Embarcações restantes: {embarcacao_player}')
    print('')
    print('')


jogador = 'PC'

inicializar()
contador = 0
continuar = 's'

while embarcacao_pc != 0 and embarcacao_player != 0:
    contador = 0
    if continuar == 's':
        if jogador == 'PC':

            linha = random.randint(0, 4)
            print(f'Computador jogou linha: {linha}!')
            coluna = random.randint(0, 9)
            print(f'Computador jogou coluna: {coluna}!')

            if jogada(linha, coluna):
                print('O computador acertou!')
            else:
                print('Nada atingido!')

            for x in vida_embarcacoesPC:
                contador += 1
                embarcacao_pc = contador
            for y in vida_embarcacoes:
                contador += 1
                embarcacao_player = contador

            visual()

            jogador = 'PLAYER'

            continuar = 's'

        else:

            linha = int(input('Digite a linha para atacar: '))
            coluna = int(input('Digite a coluna para atacar: '))

            if jogada(linha, coluna):
                print('Você acertou!')
            else:
                print('Nada atingido!')

            for x in vida_embarcacoesPC:
                contador += 1
                embarcacao_pc = contador
            for y in vida_embarcacoes:
                contador += 1
                embarcacao_player = contador

            visual()

            jogador = 'PC'
        continuar = input('Digite "s" para continuar: ')
    else:
        quit()

if embarcacao_player == 0 and continuar == 's':
    print('Você perdeu!')
else:
    print('Voce ganhou!')
