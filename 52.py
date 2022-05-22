k = 0
j = 1
lista = []
n = int(input())
while j <= n:
    soma = 0
    for i in range(1, j+1):
            if j%i==0:
                soma += i
    if soma == j*2:
        lista.append(j)
    j+=1
for l in range(0, len(lista)):
    print(lista[l])