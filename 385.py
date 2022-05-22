menor = 999
tot = totCRE = 0
mat = input()
while mat != '999':
    cre = float(input())
    tot += 1
    totCRE += cre
    if cre < menor:
        menor = cre
        matMenor = mat
    mat = input()
print(matMenor)
print('{:.2f}'.format(totCRE/tot))
