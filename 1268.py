n = int(input())
k=m=1
l = n
lista = []
while l > 0:
    for i in range(l):
        lista.append('.')
    for j in range(k):
        lista.append('*')
    print(''.join(lista))
    lista = []
    l-=1
    k+=2
k-=2
while m<=n:
    for i in range(m):
        lista.append('.')
    for l in range(k):
        lista.append('*')
    print(''.join(lista))
    lista = []
    k-=2
    m+=1