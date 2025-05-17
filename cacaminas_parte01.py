###
### Caca Minas - parte 01
###

### Configuracoes
qtBombas    = 4
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

CriaTabuleiro(Tabuleiro, Altura, Largura, 0)
MostraTabuleiro(Tabuleiro)
