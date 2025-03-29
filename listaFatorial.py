###
### preenche uma lista com o fatorial
### dos numeros de 1 ate N
###
### Prof. Filipo Novo Mór - filipomor.com
###

### Fatorial recursivo
def Fatorial(nro):
    if nro == 1: 
        return 1
    return nro * Fatorial(nro-1)
    
Quantidade = int(input("Informe o valor de N:"))
lista = [] # cria uma lista vazia

for i in range(1, Quantidade+1):
    lista.append(Fatorial(i))
    
print(lista)
    
