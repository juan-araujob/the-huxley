valor = float(input('Insira os valores das doacoes:\n'))
i = vTotal = 0
while valor > 0:
    i+=1
    vTotal += valor
    valor = float(input())
if i == 0:
    vMedio = 0
else:
    vMedio = vTotal/i
print('Total arrecadado: {:.2f}'.format(vTotal))
print('Valor medio da doacao: {:.2f}'.format(vMedio))