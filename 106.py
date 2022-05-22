n = int(input())
while n != 0:
    lista = []
    lista.append(0)
    ant = 0
    a = 1
    for i in range(n):
        lista.append(a)
        ant = a
        a += ant
    n = int(input())