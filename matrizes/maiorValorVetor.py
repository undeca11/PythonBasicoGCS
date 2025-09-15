##############################################################
### Gera um vetor com valores aleatorios e encontra o      ###
### valor gerado, indicando a sua posicao                  ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho do vetor (N): "))

vetor = [random.randint(1, N * N) for _ in range(N)]

maior_valor = max(vetor)
posicao = vetor.index(maior_valor)

print("\nVetor:", vetor)
print("Maior valor:", maior_valor)
print("Posição do maior valor:", posicao)
