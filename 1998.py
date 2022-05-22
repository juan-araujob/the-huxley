v=0
while v == 0:
    n1 = int(input())
    if n1 < 1 or n1 > 9:
        print('Insira um número inicial entre 1 e 9')
    else:
        v=1
v=0
while v == 0:
    n2 = int(input())
    if n2 < 1 or n2 > 9:
        print('Insira um número final entre 1 e 9')
    else:
        v=1
if n1 > n2:
    print('Nenhuma tabuada nesse intervalo')
for i in range(n1, n2+1):
    for j in range(1, 10):
        print('{} x {} = {}'.format(i, j, i*j))
    print('')

