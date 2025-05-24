###
### Caca Minas - parte 02
###
import random as rd

### Configuracoes
qtBombas    =  7
qtBandeiras =  0
Largura     = 10 # qt de colunas do tabuleiro
Altura      = 10 # qt de linhas do tabuleiro
valorBomba  =  9 # valor da bomba no tabuleiro
celAberta   = 1
celFechada  = 0
celMarcada  = True
celVazia    = 0
Tabuleiro   = [] # contem espaco vazio, bomba ou contagem
TabStatus   = [] # indica de posicao esta aberta (celAberta) ou fechada (celFechada)
TabMarcacao = [] # indica se posicao recebeu bandeira (celMarcada) ou nao (!celMarcada)

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

def MostraTabuleiroCompleto(tabuleiro, tabStatus, tabMarcacao):
    for y in range(0, len(tabuleiro)):
        print(tabuleiro[y],   end=" ")
        #print(tabStatus[y],   end=" ")
        # troca os '1' por '.' e os '0' por '#', além de remover as aspas simples (com o join)
        print(' '.join([str(s).replace("1", ". ").replace("0", "# ") for s in tabStatus[y]]), end = " ")
        print(tabMarcacao[y], end=" ")
        print()
    print()

###
### Popula o tabuleiro com a quantidade de bombas configurada
###
def CriaBombas(tabuleiro, qtBombas, valorBomba):
    posicoes = [(x, y) for x in range(Largura) for y in range(Altura)]
    rd.shuffle(posicoes)  # Embaralha as posições possíveis

    for i in range(qtBombas):
        posX, posY = posicoes[i]
        tabuleiro[posX][posY] = valorBomba

'''
###
### Contador de Bombas e atualiza o Tabuleiro
###
def ContaBombas(tabuleiro, valorBomba):
    for y in range(0, len(tabuleiro)):         # itera pelas linhas
        for x in range(0, len(tabuleiro[y])):  # itera pelas colunas
            if tabuleiro[y][x] != valorBomba:  # se a posicao nao contiver uma bomba
                cont = 0
                # olha acima, se possivel
                if y > 0:
                    if tabuleiro[y-1][x] == valorBomba: cont += 1
                # olha abaixo, se possivel
                if y < len(tabuleiro)-1:
                    if tabuleiro[y+1][x] == valorBomba: cont += 1
                # olha para a direita, se possivel
                if x < len(tabuleiro[y])-1:
                    if tabuleiro[y][x+1] == valorBomba: cont += 1
                # olha para a esquerda, se possivel
                if x > 0:
                    if tabuleiro[y][x-1] == valorBomba: cont += 1
                # olha para a diagonal superior direita, se possivel
                if y > 0 and x < len(tabuleiro[y])-1:
                    if tabuleiro[y-1][x+1] == valorBomba: cont += 1
                # olha para a diagonal superior esquerda, se possivel
                if y > 0 and x > 0:
                    if tabuleiro[y-1][x-1] == valorBomba: cont += 1
                # olha para a diagonal inferior direita, se possivel
                if y < len(tabuleiro)-1 and x < len(tabuleiro[y])-1:
                    if tabuleiro[y+1][x+1] == valorBomba: cont += 1
                # olha para a diagonal inferior esquerda, se possivel
                if y < len(tabuleiro)-1 and x > 0:
                    if tabuleiro[y+1][x-1] == valorBomba: cont += 1

                # atualiza o valor de bombas ao redor na celula
                tabuleiro[y][x] = cont
'''

###
### Contador de Bombas e atualiza o Tabuleiro
###
def ContaBombas(tabuleiro, valorBomba):
    # A função começa definindo uma lista de offsets que representam os oito possíveis
    # deslocamentos em torno de uma célula específica (direções que precisam ser verificadas:
    # acima, baixo, esquerda, direita e as quatro diagonais)
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    # Cada tupla (dy, dx) representa um deslocamento relativo à posição atual (y, x) no tabuleiro.

    # A função percorre cada célula do tabuleiro usando loops duplos para linhas (y) e colunas (x).
    for y in range(len(tabuleiro)):
        for x in range(len(tabuleiro[y])):
            if tabuleiro[y][x] != valorBomba: # Para cada célula, ela verifica se não contém uma bomba.
                                              # Se a célula contém uma bomba, ela é ignorada.

                # A função calcula quantas bombas existem ao redor da célula atual
                # usando uma expressão sum. Para cada offset, ela verifica se a
                # célula adjacente existe dentro dos limites do tabuleiro e se contém uma bomba.
                cont = sum(
                    1 for dy, dx in offsets
                    # 0 <= y + dy < len(tabuleiro): Garante que o novo y está dentro dos limites do tabuleiro.
                    # 0 <= x + dx < len(tabuleiro[0]): Garante que o novo x está dentro dos limites do tabuleiro.
                    if 0 <= y + dy < len(tabuleiro) and 0 <= x + dx < len(tabuleiro[0])
                    and tabuleiro[y + dy][x + dx] == valorBomba #Verifica se a célula no deslocamento atual contém uma bomba.
                )
                tabuleiro[y][x] = cont # atualiza o contador de bombas para a celula atual


def AbreArea(tabuleiro, tabStatus, linha, coluna, celulaAnteriorVazia):

    cont = 0    # contador de celulas abertas

    if tabStatus[linha][coluna] != celAberta and tabuleiro[linha][coluna] == celVazia:

        tabStatus[linha][coluna] = celAberta
        cont += 1

        # acima, se possivel
        if linha > 0 and tabStatus[linha-1][coluna] != celAberta:
            cont += AbreArea(tabuleiro, tabStatus, linha-1, coluna, True)
        # abaixo, se possivel
        if linha < len(tabuleiro)-1 and tabStatus[linha+1][coluna] != celAberta:
            cont += AbreArea(tabuleiro, tabStatus, linha+1, coluna, True)
        # esquerda, se possivel
        if coluna > 0 and tabStatus[linha][coluna-1] != celAberta:
            cont += AbreArea(tabuleiro, tabStatus, linha, coluna-1, True)
        # direita, se possivel
        if coluna < len(tabuleiro)-1 and tabStatus[linha][coluna+1] != celAberta:
            cont += AbreArea(tabuleiro, tabStatus, linha, coluna+1, True)

    #elif tabStatus[linha][coluna] != celAberta and tabuleiro[linha][coluna] > 0 and tabuleiro[linha][coluna] <= 8 and celulaAnteriorVazia == True:
    elif tabStatus[linha][coluna] != celAberta and celulaAnteriorVazia == False:   # expande a area, excluindo celulas com contador
    #elif tabStatus[linha][coluna] != celAberta and celulaAnteriorVazia == True:    # expande a area, incluindo uma camada de celulas com contador
        tabStatus[linha][coluna] = celAberta
        cont += 1

    return cont


CriaTabuleiro(Tabuleiro, Altura, Largura, 0)
CriaBombas(Tabuleiro, qtBombas, valorBomba)
ContaBombas(Tabuleiro, valorBomba)
#MostraTabuleiro(Tabuleiro)

CriaTabuleiro(TabStatus, Altura, Largura, 0)   # todas as celulas fechadas
CriaTabuleiro(TabMarcacao, Altura, Largura, 0) # nenhuma celula marcada

#MostraTabuleiroCompleto(Tabuleiro, TabStatus, TabMarcacao)
contador = AbreArea(Tabuleiro, TabStatus, 5, 5, False) # teste
MostraTabuleiroCompleto(Tabuleiro, TabStatus, TabMarcacao)

print(F"\nqt celulas abertas: {contador}\n")