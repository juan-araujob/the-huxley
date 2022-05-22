L = int(input())
if 1 <= L <= 20:
    P = 20 + (L**3)
elif 21 <= L <= 40:
    P = 8000 + (L-10)**2
elif 41 <= L <= 60:
    P = 9000 + 5*L
elif 61 <= L <= 80:
    P = 9300 + 2*L
else:
    P = 9500 + L
print('Potencia de : {} W'.format(P))