##############################################################
###           Calcula o produto vetorial escalar           ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

def ProdutoEscalarVetorialPython(vetor1, vetor2):
    return sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))    


def ProdutoEscalarVetorialAnalitico(vetor1, vetor2):
    produto_escalar = 0
    print("\n--- Cálculo passo a passo ---")
    for i in range(N):
        multiplicacao = vetor1[i] * vetor2[i]
        produto_escalar += multiplicacao
        print(f"Elemento {(i+1):2}: {vetor1[i]:3} * {vetor2[i]:3} = {multiplicacao:3} | Soma parcial = {produto_escalar:6}")

    return produto_escalar


# Solicita o tamanho do vetor
N = int(input("Digite o tamanho dos vetores (N): "))

# Gera os vetores com valores aleatórios entre 1 e N*N
vetor1 = [random.randint(1, N * N) for _ in range(N)]
vetor2 = [random.randint(1, N * N) for _ in range(N)]

# Calcula o produto escalar no estilo Python
produto_escalar = ProdutoEscalarVetorialPython(vetor1, vetor2)

# Exibe resultados
print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Produto escalar (estilo Python) =", produto_escalar)

# Calcula o produto escalar no estilo analitico, passo a passo
produto_escalar = ProdutoEscalarVetorialAnalitico(vetor1, vetor2)

# Exibe resultados
print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Produto escalar (analitico) =", produto_escalar)

