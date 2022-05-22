quant = int(input())
cidade = input()
quartos = int(input())
v = 0
if cidade.lower() == 'pipa':
    if quartos == 2:
        v = 600+75*quant
    else:
        v = 900+75*quant
elif cidade.lower() == 'fortaleza':
    if quartos == 3:
        v = 950+60*quant
    else:
        v = 1120+60*quant
print('{:.2f}'.format(v))
print('{:.2f}'.format(v/quant))