###
### vetor com valores aleatorios
### Prof. Filipo Mór

import random
N = 10
lista = [0]*N

for i in range(len(lista)):
    lista[i] = random.randint(0, N)
    
print(f"\n lista o vetor inteiro: {lista}")

print(f"\n Lista o valor de cada posicao\n")
for i in range(len(lista)):
    print(f"Posicao[{i}]: {lista[i]}")

