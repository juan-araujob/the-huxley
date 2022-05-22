res1 = input('Telefonou para a vitima?\n')
res2 = input('Esteve no local do crime?\n')
res3 = input('Mora perto da vitima?\n')
res4 = input('Devia para a vitima?\n')
res5 = input('Ja trabalhou com a vitima?\n')
verdade = 0
if res1 == 'True':
    verdade += 1
if res2 == 'True':
    verdade += 1
if res3 == 'True':
    verdade += 1
if res4 == 'True':
    verdade += 1
if res5 == 'True':
    verdade += 1
if verdade < 2:
    print('Inocente')
elif verdade == 2:
    print('Suspeita')
elif 3 <= verdade <= 4:
    print('Cumplice')
else:
    print('Assassino')


