PSNR = int(input())
enq = input()
exp = input()
if PSNR >= 80:
    if enq == 'excelente' or enq == 'bom':
        if exp == 'bem exposta':
            print('para imprimir')
        else:
            print('boa')
    else:
        print('marromeno')
elif 50 <= PSNR < 80:
    if enq == 'excelente' and exp == 'bem exposta':
        print('boa')
    else:
        print('marromeno')
else:
    if enq == 'excelente' and exp == 'bem exposta':
        print('marromeno')
    else:
        print('lixo')