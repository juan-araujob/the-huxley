quant = int(input())
casasMultadas = multaTOTAL= 0
while quant != 999:
    if quant > 2:
        multaTOTAL += (quant-2)*12.89
        casasMultadas += 1
    quant = int(input())
print('{:.2f}'.format(multaTOTAL))
print(casasMultadas)