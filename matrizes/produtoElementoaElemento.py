##############################################################
###             Produto elemento a elemento                ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho dos vetores (N): "))

vetor1 = [random.randint(1, N * 3) for _ in range(N)]
vetor2 = [random.randint(1, N * 3) for _ in range(N)]

vetor_produto = [v1 * v2 for v1, v2 in zip(vetor1, vetor2)]

print("\nVetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor Produto:", vetor_produto)
