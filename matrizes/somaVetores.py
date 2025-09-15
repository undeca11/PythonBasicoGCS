##############################################################
### Gera um vetor com a soma dos dois vetores originais,   ###
### posicao a posicao                                      ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho dos vetores (N): "))

vetor1 = [random.randint(1, N * N) for _ in range(N)]
vetor2 = [random.randint(1, N * N) for _ in range(N)]

vetor_soma = [v1 + v2 for v1, v2 in zip(vetor1, vetor2)]

print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor Soma:", vetor_soma)
