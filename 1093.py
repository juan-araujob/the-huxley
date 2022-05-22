C = V = totC = totV = maiorCompra = 0
menorIdade = 999
cont = 'S'
while cont == 'S':
    idade = int(input())
    vCompra = float(input())
    tPagamento = input()
    if tPagamento == 'C':
        C += vCompra
        totC += 1
    elif tPagamento == 'V':
        V += vCompra
        totV += 1
    if idade < menorIdade:
        menorIdade = idade
    if vCompra > maiorCompra:
        maiorCompra = vCompra
    cont = input()
print(totC+totV)
print(round(V, 2))
print(round(C, 2))
print(menorIdade)
print('{:.2f}'.format(maiorCompra))
if totV == 0:
    print(0)
else:
    print('{:.2f}'.format(V/totV))