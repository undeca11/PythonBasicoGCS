###
### Fatorial (recursivo e iterativo)
### Prof. Filipo Mór

NRO = int(input(f"\n Informe um numero: "))

# fatorial recursivo
def fatorial(n):
    if n == 0:
        return 1
    resultado = n * fatorial(n-1)
    return resultado
    
#fatorial iterativo
def fatorial2(n):
    nro = 1
    valor = 1
    while nro <= n:
        valor = valor * nro
        nro = nro + 1
    return valor

resultado = fatorial(NRO)
print(f"o fatorial [recursivo] de {NRO} eh {resultado}")

resultado = fatorial2(NRO)
print(f"o fatorial [iterativo] de {NRO} eh {resultado}")
