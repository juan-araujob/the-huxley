vDoacao = int(input())
vMensal = vFuturos = 0
while vDoacao > 0:
    v=0
    while v==0:
        op = int(input())
        if op == 1:
            vMensal += vDoacao
            v=1
        elif op == 2:
            v = 0
            while v == 0:
                m = int(input())
                if 2<=m<=12:
                    vMensal += vDoacao
                    vFuturos += vDoacao*(m-1)
                    v = 1
                else:
                    print('Favor digitar valor entre 2 e 12, inclusive')
        else:
            print('Valor invalido')
    vDoacao = int(input())
print('Total arrecadado para agora: R$ {:.2f}'.format(vMensal))
print('Total arrecadado para meses futuros: R$ {:.2f}'.format(vFuturos))