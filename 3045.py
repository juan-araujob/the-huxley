num = int(input())
while num != 0:
    novoNum = str(num)
    a = len(novoNum)-1
    n1 = int(novoNum[a])
    if num > 10:
        n2 = int(novoNum[:a])
    else:
        n2 = 0
    numeroFinal = n2 + n1*5
    if numeroFinal%7==0:
        print('S')
    else:
        print('N')
    num = int(input())