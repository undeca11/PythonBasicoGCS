###
### Preenche lista com n primeiros numeros primos
###
### Prof. Filipo Novo Mór
###

# Devolve True se o nro for primo
def EhPrimo(nro):
    for i in range(2, nro-1):
        if nro % i == 0:
            return False
    return True
    
Quantidade = int(input("Quantos numeros primos voce deseja?"))
lista = [0]*Quantidade # cria lista preenchida com valores zero do tamanho necessario
pos   = 0 # controla a proxima posicao da lista que recebera um numero primo
cont  = 0 # contador de iteracoes

while(pos < Quantidade):
    if EhPrimo(cont + 1):
        lista[pos] = cont + 1
        pos += 1
    cont += 1
    
print(f"Os {Quantidade} primeiros numeros primos sao: {lista}")
