##############################################################
###            Gera matriz com valores crescentes          ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

# Lê o tamanho da matriz
N = int(input("Digite o valor de N: "))

# Cria a matriz com valores crescentes
matriz = [[i * N + j + 1 for j in range(N)] for i in range(N)]

# Exibe a matriz
for linha in matriz:
    print(linha)
