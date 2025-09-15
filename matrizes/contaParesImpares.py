##############################################################
###           Contagem de pares e impares no vetor         ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

import random

N = int(input("Digite o tamanho do vetor (N): "))

vetor = [random.randint(1, N * 10) for _ in range(N)]

pares = sum(1 for v in vetor if v % 2 == 0)
impares = N - pares

print("\nVetor:", vetor)
print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
