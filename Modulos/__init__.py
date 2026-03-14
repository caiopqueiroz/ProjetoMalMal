from rich import print
from rich.panel import Panel
from time import sleep


#def comecarNovoJogo():


def qJogadores(nume):
    jogadores = list()


    print(Panel(f'Muito bem! Partida com {nume} jogadores.', width=50))
    for contador in range(0, nume):
        jogadores.append(str(input(f' Nome {contador}: ')).strip().title())
    sleep(1)
    print(Panel('Tudo certo!', width=50))
    return jogadores


def lPontos(lJogadores):
    pontos = list()


    for contador in range(0, len(lJogadores)):
        pontos.append(0)
    return pontos


def mostrarPlacar(lJogadores, lPontos):
    print(Panel('Placar', width=50))
    for jogador in lJogadores:
        print(f'{jogador:<10}', end='')
    print()
    print('=' * (len(lJogadores) * 10))
    for jogador in lPontos:
        print(f'{jogador:<10}', end='')
    print()


def somarPontos(lJogadores, lPontos):
    qJogadores = len(lPontos)


    print(Panel('Fim da Rodada!', width=50))
    for contador in range(0, qJogadores):
        lPontos[contador] += (int(input(f' Pontos de {lJogadores[contador]}: ')))
        if lPontos[contador] >= 200:
            lPontos[contador] = 'BOOM!!'
    return lPontos


def interfaceMalMal():
    while True:
        print(Panel('[ 1 ] Começar Novo Jogo\n'
                    '[ 2 ] Inserir Pontuação da Rodada\n'
                    '[ 3 ] Mostrar Placar\n'
                    '[ 4 ] Encerrar Programa', title='MAL MAL v1.0', width=50))
        print()
        print()
        while True:
            comando = int(input('Insira aqui sua opção: '))
            if not 1 <= comando <= 4:
                print('\033[31;7;1m !ERRO! Por favor, insira uma opção válida. \033[m')
            else:
                break
        if comando == 1:
            print()
            print()
            sleep(1)
            print(Panel('Quantas pessoas vão jogar?', width=50))
            nJogadores = int(input(' Número de jogadores: '))
            sleep(1)
            j = qJogadores(nJogadores)
            p = lPontos(j)
            print()
            print()
            sleep(2)
        if comando == 2:
            try:
                sleep(1)
                somarPontos(j, p)
                sleep(1)
                mostrarPlacar(j, p)
                print()
                print()
                sleep(2)
            except:
                print('\033[31;7;1m !ERRO! Nenhum Jogo Inicado Ainda. \033[m')
                print()
                print()
                sleep(2)
        if comando == 3:
            try:
                sleep(1)
                mostrarPlacar(j, p)
                print()
                print()
                sleep(2)
            except:
                print('\033[31;7;1m !ERRO! Nenhum Jogo Inciado Ainda. \033[m')
                print()
                print()
                sleep(2)
        if comando == 4:
            print('\033[31;7;1m Programa Encerrado \033[m')
            break



















