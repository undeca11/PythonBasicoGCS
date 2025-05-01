###
### Preenche uma lista com os n primeiros numeros primos
###
### Prof. Filipo Novo Mór
###

# Devolve True se o nro for primo
def EhPrimo(nro):
    for i in range(2, nro-1):
        if nro % i == 0:
            return False
    return True
    
Quantidade               = int(input("Quantos numeros primos voce deseja? "))
lista                    = [0]*Quantidade # cria lista preenchida com valores zero do tamanho necessario
pos                      = 0 # controla a proxima posicao da lista que recebera um numero primo
numero_a_ser_verificado  = 2 # 0 e 1 nao sao primos

while(pos < Quantidade):
    if EhPrimo(numero_a_ser_verificado):
        lista[pos] = numero_a_ser_verificado
        pos += 1
    numero_a_ser_verificado += 1
    
print(f"Os {Quantidade} primeiros numeros primos sao: {lista}")
