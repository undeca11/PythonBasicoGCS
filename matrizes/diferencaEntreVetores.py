##############################################################
###                Diferença entre vetores                 ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho dos vetores (N): "))

vetor1 = [random.randint(1, N * 4) for _ in range(N)]
vetor2 = [random.randint(1, N * 4) for _ in range(N)]

vetor_diferenca = [v1 - v2 for v1, v2 in zip(vetor1, vetor2)]

print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor Diferença (V1 - V2):", vetor_diferenca)
