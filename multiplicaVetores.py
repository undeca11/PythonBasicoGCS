###
### preenche vetores com valores aleatorios entre 1 e N
### em seguida, preenche o vetor3 com a multiplicacao
### de cada posicao correspondente em vetor1 e vetor2
###
### Prof. Filipo Mór

import random

# quantidade de valores
N = 10

# cria 3 listas vazias
vetor1 = []
vetor2 = []
vetor3 = [] 

# preenche vetor1 e vetor2 com numeros aleatorios entre 1 e N
vetor1 = [random.randint(1, N) for i in range(N)]
vetor2 = [random.randint(1, N) for i in range(N)]

# preenche cada posicao de vetor3 com o produto das 
# posicoes correspondentes de vetor1 e vetor2
vetor3 = [vetor1[i] * vetor2[i] for i in range(N)]

print(vetor1)
print(vetor2)
print(vetor3)

