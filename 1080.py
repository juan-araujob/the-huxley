med = input()
t = float(input())
if med == 'C' and t >= -273:
    F = t*9/5 + 32
    K = t + 273.15
    print('{:.2f} F'.format(F))
    print('{:.2f} K'.format(K))
elif med == 'F' and t >= -459.67:
    C = (t-32)*5/9
    K = C + 273.15
    print('{:.2f} C'.format(C))
    print('{:.2f} K'.format(K))
elif med == 'K' and t >= 0:
    C = t-273.15
    F = C * 9/5 + 32
    print('{:.2f} C'.format(C))
    print('{:.2f} F'.format(F))
else:
    print('Valor de temperatura abaixo do minimo')
