import random
import copy

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
                if contagem:
                    cont += 1
                    linha.append(cont)
                else:
                    linha.append(random.randint(menorValor, maiorValor))
            grade.append(linha)
        matriz.append(grade)
    return matriz

# Criando a matriz de exemplo
Ma = PopulaMatriz(N, N-1, N-2, 1, 30, True)
MostraMatriz(Ma, "Matriz 3D Inicial")

# Exercício 1: Soma de todos os elementos
def SomaElementos(matriz):
    soma = 0
    for z in matriz:
        for y in z:
            for valor in y:
                soma += valor
    return soma

print("\nExercício 1 - Soma de todos os elementos:", SomaElementos(Ma))

# Exercício 2: Valor máximo e mínimo
def EncontraMaxMin(matriz):
    max_val = float('-inf')
    min_val = float('inf')
    for z in matriz:
        for y in z:
            for valor in y:
                if valor > max_val:
                    max_val = valor
                if valor < min_val:
                    min_val = valor
    return max_val, min_val

maximo, minimo = EncontraMaxMin(Ma)
print(f"\nExercício 2 - Valor Máximo: {maximo}, Valor Mínimo: {minimo}")

# Exercício 3: Transpor cada fatia
def TransporFatias(matriz):
    matriz_transposta = []
    for z in matriz:
        transposta = list(zip(*z))
        # Convertendo tuplas de volta a listas
        transposta = [list(linha) for linha in transposta]
        matriz_transposta.append(transposta)
    return matriz_transposta

Ma_transp = TransporFatias(Ma)
MostraMatriz(Ma_transp, "Ex.3: Matriz Transposta de Cada Fatia")

# Exercício 4: Média dos elementos de uma camada específica
def MediaCamada(matriz, camada):
    if camada < 0 or camada >= len(matriz):
        return None
    soma = 0
    count = 0
    for y in matriz[camada]:
        for valor in y:
            soma += valor
            count += 1
    return soma / count if count > 0 else None

camada_escolhida = 1  # exemplo: segunda camada
media = MediaCamada(Ma, camada_escolhida)
print(f"\nExercício 4 - Média da camada {camada_escolhida}: {media:.2f}")

# Exercício 5: Adicionar um valor constante a todos elementos
def AdicionarValor(matriz, valor_adicao):
    for z in range(len(matriz)):
        for y in range(len(matriz[z])):
            for x in range(len(matriz[z][y])):
                matriz[z][y][x] += valor_adicao
    return matriz

valor_a_adicionar = 10
# Pode usar copy.deepcopy para copiar toda a estrutura
Ma_copia = copy.deepcopy(Ma)

# Agora, adicionamos o valor
Ma_modificada = AdicionarValor(Ma_copia, valor_a_adicionar)
MostraMatriz(Ma_modificada, f"Ex.5: Matriz após adicionar {valor_a_adicionar}")