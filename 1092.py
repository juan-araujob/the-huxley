m = f = sM = sF = sMaiorSalario = 0
for i in range(10):
    salario = float(input())
    sexo = input()
    if sexo == 'm':
        m += 1
        sM += salario
    elif sexo == 'f':
        f += 1
        sF += salario
    if salario > sMaiorSalario:
        sMaiorSalario = salario
        sRico = sexo
print(m)
print(f)
print('{:.1f}'.format((sM+sF)/(m+f)))
print(sRico)
print('{:.1f}'.format(sM/m))
