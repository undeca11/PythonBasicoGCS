import random

N = 5 # quantidade de linhas
M = 5 # quantidade de colunas

def MostraMatriz(titulo, matriz):
    print(f"\n{titulo}")
    print("  ", end="")
    [print(f" {i:4d}", end="") for i in range(M)]
    print("\n", end="")
    for i in range(N):
        print(i, end=" ")
        for j in range(M):
            print(f" {matriz[i][j]:4d}", end="" )
        print("\n", end="")

def PopulaMatriz(qtLinhas, qtColunas, menorValor, maiorValor):
    matriz = [[0] * qtColunas for i in range(qtLinhas)] # cria a matriz populada com zeros
    for i in range(qtLinhas): # preenche a matriz com inteiros aleatorios
        for j in range(qtColunas):
            matriz[i][j] = random.randint(menorValor, maiorValor)
    return matriz


matriz = PopulaMatriz(N, M, 1, N*M)


MostraMatriz("Matriz original", matriz)

# preenche a diagonal principal da matriz com zeros
for i in range(N):
    matriz[i][i] = 0
MostraMatriz("0s na diagonal principal", matriz)

#preenche a diagonal secundaria da matriz com -1
for i in range(N):
    matriz[i][N-i-1] = -1
MostraMatriz("-1 na diagonal secundaria", matriz)

matriz2 = PopulaMatriz(N, M, 0, 0)
MostraMatriz("M2 zerada", matriz2)