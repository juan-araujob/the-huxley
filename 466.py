maior = -1
cidade = input()
cidadeDeDESTINO = 'SEM DESTINO'
while cidade.lower() != 'fim':
    km = int(input())
    passagem = float(input())
    passagem = passagem * 2
    if passagem <= 300:
        if km > maior:
          maior = km
          cidadeDeDESTINO = cidade.upper()
    cidade = input()
print(cidadeDeDESTINO)