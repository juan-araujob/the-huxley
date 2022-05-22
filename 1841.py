menor = 99999
maior = -1
totCestas = jog = 0
nome = input()
if nome != 'sair':
    while nome != 'sair':
        cestas = int(input())
        totCestas += cestas
        jog += 1
        if cestas <= menor:
            menor = cestas
            menorJog = nome
        if cestas >= maior:
            maior = cestas
            maiorJog = nome
        nome = input()
    print(menorJog)
    print(maiorJog)
    print('{:.2f}'.format(totCestas/jog))
else:
    print('Nenhum jogador foi registrado.')
