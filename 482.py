meta = totCartas = 0
for i in range(7):
    cartas = int(input())
    if cartas >= 100:
        meta += 1
    totCartas += cartas
print(meta)
print('{:.0f}'.format(totCartas/7))