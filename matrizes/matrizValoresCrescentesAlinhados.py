##############################################################
###  Gera matriz com valores crescentes e com alinhamento  ###
##############################################################
### Prof. Filipo Mor - github.com/ProfessorFilipo          ###
##############################################################

def gerar_matriz(N):
    # Calcula o número de casas (M) automaticamente
    M = len(str(N * N))

    # Cria a matriz com valores crescentes
    matriz = [[i * N + j + 1 for j in range(N)] for i in range(N)]

    # Exibe a matriz formatada
    for linha in matriz:
        for valor in linha:
            print(f"{valor:>{M}}", end=" ")
        print()

    return matriz


# Exemplo de uso
if __name__ == "__main__":
    N = int(input("Digite o valor de N: "))
    gerar_matriz(N)
