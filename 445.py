dias = int(input())
km = int(input())
if km > (dias*100):
    vTotal = dias*90 + ((km-dias*100)*12)
else:
    vTotal = dias*90
print('{:.2f}'.format(vTotal))
