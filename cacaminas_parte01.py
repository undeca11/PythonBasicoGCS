###
### Caca Minas - parte 01
###
import random as rd

### Configuracoes
qtBombas    = 5
qtBandeiras = 0
Largura     = 5 # qt de colunas do tabuleiro
Altura      = 5 # qt de linhas do tabuleiro
valorBomba  = 9 # valor da bomba no tabuleiro
Tabuleiro   = []
TabStatus   = []
TabMarcacao = []

###
### Cria o Tabuleiro
###
def CriaTabuleiro(tabuleiro, altura, largura, valorPadrao):

    for x in range(0, largura):
        linha = []
        for y in range(0, altura):
            linha.append(valorPadrao)
        tabuleiro.append(linha)

### teste
def MostraTabuleiro(tabuleiro):
    for x in range(0, len(tabuleiro)):
        print(tabuleiro[x])

###
### Popula o tabuleiro com a quantidade de bombas configurada
###
def CriaBombas(tabuleiro, qtBombas, valorBomba):
    cont = 0
    for x in range(0, qtBombas):
        posLivre = False
        while not posLivre:
            posLivre = True
            posX = rd.randint(0, Largura-1)
            posY = rd.randint(0, Altura-1)
            if tabuleiro[posX][posY] == valorBomba:
                posLivre = False
            print(posX, posY)
            cont += 1
        tabuleiro[posX][posY] = valorBomba
        print(f"sorteios: {cont}")

CriaTabuleiro(Tabuleiro, Altura, Largura, 0)
CriaBombas(Tabuleiro, qtBombas, valorBomba)
MostraTabuleiro(Tabuleiro)
