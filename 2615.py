divida = int(input())
valorMES = int(input())
while divida > 0:
    print('(antes) {}'.format(divida))
    divida = divida - valorMES
    if divida < 0:
        print('(depois) 0')
    else:
        print('(depois) {}'.format(divida))
