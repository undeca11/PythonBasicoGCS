###############################################################
#### Cria uma matriz 3D (ou N-D)                           ####
#### popula a matriz com valores sequenciais ou aleatórios ####
###############################################################
#### Prof. Filipo Novo Mór - filipomor.com                 ####
###############################################################
import random
N = 5

def MostraMatriz(matriz, titulo):
    print("\n" + titulo)
    for y in range(len(matriz[0])):
        for z in range(len(matriz)):
            for x in range(len(matriz[0][y])):
                print(f" {matriz[z][y][x]:3d} ", end='')
            print("   ", end="")
        print()

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

Ma = PopulaMatriz(N, N-1, N-2, 1, 30, True)

MostraMatriz(Ma, "Matriz 3D")