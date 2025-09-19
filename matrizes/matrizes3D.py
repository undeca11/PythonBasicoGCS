###############################################################
#### Cria uma matriz 3D (ou N-D)                           ####
#### popula a matriz com valores sequenciais ou aleatórios ####
###############################################################
#### Prof. Filipo Novo Mór - filipomor.com                 ####
###############################################################
import random
N = 5

###
### Devolve o maior valor numérico existente na matriz.
### Funciona apenas em matrizes 3D
###
def MaiorValor(matriz):
    maior = matriz[0][0][0]
    for z in range(len(matriz)):
        for y in range(len(matriz[z])):
            for x in range(len(matriz[z][y])):
                if matriz[z][y][x] > maior:
                    maior = matriz[z][y][x]
    return maior

###
### Devolve a quantidade de digitos do número inteiro dado
###
def ContaDigitos(numero):
    return len(str(abs(numero)))

###
### Mostra a matriz 3D na tela, com as faces lado a lado
###
def MostraMatriz(matriz, titulo):
    qtDigitos = ContaDigitos(MaiorValor(matriz))
    print("\n" + titulo)
    for y in range(len(matriz[0])):
        for z in range(len(matriz)):
            for x in range(len(matriz[0][y])):
                #print(f" {matriz[z][y][x]:3d} ", end='')
                print(f" {matriz[z][y][x]:>{qtDigitos}} ", end='')
            print("   ", end="")
        print()

###
### Mostra na tela a matriz 2D com
### as faces da matriz 3D inscritas e ajustadas
### internamente.
###
def MostraGradeTela(matriz, titulo, mostraMarcacoes, qtDigitos):
    print(F"\n{titulo}")
    qtLinhas  = len(matriz)
    qtColunas = len(matriz[0])
    for y in range(qtLinhas):
        for x in range(qtColunas):
            if matriz[y][x] == ".":
                if mostraMarcacoes:
                    # configura a quantidade de '.'s para a quantidade de digitos esperada
                    print(F" {'.' * qtDigitos} ", end="")
                else:
                    print(F" {' ' * qtDigitos} ", end="")
            else:
                print(f" {int(matriz[y][x]):>{qtDigitos}} ", end='')
        print()

###
### Mostra a matriz 3D inscrita em uma matriz 2D,
### colocando as faces lado a lado, porém, com um
### espacamento vertical e horizontal configuraveis
### entre elas.
###
###
### configura o tamanho da grade na tela, considerando as dimensoes
### da matriz original e a quantidade de faces
###
###    +---+
###    |   |   +---+
###    +---+   |   |   +---+
###            +---+   |   |
###                    +---+
def MostraMatrizDegrau(matriz, titulo, mostraMarcacoes):

    qtFatias     = len(matriz)
    qtLinhas     = len(matriz[0])
    qtColunas    = len(matriz[0][0])
    espacamentoH = 1
    espacamentoV = 1
    qtDigitos    = ContaDigitos(MaiorValor(matriz))

    larguraGrade = (qtFatias * qtColunas + 2 * espacamentoH + (qtFatias-1) * espacamentoH)
    alturaGrade  = qtLinhas + ((qtFatias-1) * espacamentoV) + 2 * espacamentoV

    ### teste
    ###print(F"\n{titulo}\nFaces: {qtFatias}\nLinhas: {qtLinhas}\nColunas: {qtColunas}")
    ###print(F"\nlargura total: {larguraGrade}\naltura total: {alturaGrade}")

    # cria a matriz 2D de acordo com as dimensoes calculadas
    # para comportar as faces da matriz 3D corretamente
    # posicionadas e espacadas entre si e em relacao
    # aos limites superior, inferior e laterais da matriz 2D
    gradeTela = []
    for y in range(alturaGrade):
        linha = []
        for x in range(larguraGrade):
            linha.append('.')
        gradeTela.append(linha)

    # inscreve ("carimba", ou "projeta") cada face da matriz 3D
    # na sua posicao correspondente dentro da matriz 2D
    posX = espacamentoH
    posY = espacamentoV
    for z in range(qtFatias):
        for y in range(qtLinhas):
            for x in range(qtColunas):
                gradeTela[posY+y][posX+x] = matriz[z][y][x]
        posX += espacamentoH + qtColunas
        posY += espacamentoV

    MostraGradeTela(gradeTela, titulo, mostraMarcacoes, qtDigitos)

###
### Popula a matriz 3D dada da seguinte forma:
###    parametro contagem == true:  numera as celulas da matriz com valores
###                                 inteiros crescentes, iniciando de 'menorValor'
###    parametro contagem == False: popula as celulas da matriz com valores
###                                 sorteados entre 'menorValor' e 'maiorValor'
###
def PopulaMatriz(qtColunas, qtLinhas, qtFatias, menorValor, maiorValor, contagem):
    cont = 0
    matriz = []
    for z in range(qtFatias):
        grade = []
        for y in range(qtLinhas):
            linha = []
            for x in range(qtColunas):
                if(contagem==True):
                    cont += 1
                    linha.append(cont)
                else:
                    linha.append(random.randint(menorValor, maiorValor))
            grade.append(linha)
        matriz.append(grade)
    return matriz

#Ma = PopulaMatriz(N, N-1, N-2, 1, 100, False)
Ma = PopulaMatriz(N, N, N, 1, 30, True)

MostraMatrizDegrau(Ma, "Matriz Degrau", True)
MostraMatriz(Ma, "Matriz 3D com faces lado a lado")