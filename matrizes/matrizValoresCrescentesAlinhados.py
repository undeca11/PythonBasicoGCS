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

'''
Explicando a declaracao  {valor:>{M}}

Dentro das chaves temos três elementos:
   valor → é o número que será exibido.
   : → separa a variável de suas regras de formatação.
   >{M} → significa:
      > → alinhamento à direita.
      {M} → largura mínima da célula, ou seja, quantos caracteres o número vai ocupar.
Se o número tiver menos dígitos que M, ele é preenchido com espaços à esquerda.
'''
