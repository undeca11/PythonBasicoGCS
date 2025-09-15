##############################################################
### Produto Vetorial Escalar, utilizando o proprio vetor   ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho do vetor (N): "))

vetor = [random.randint(1, N * N) for _ in range(N)]

produto_escalar = sum(v * v for v in vetor)

print("\nVetor:", vetor)
print("Produto escalar do vetor consigo mesmo:", produto_escalar)
