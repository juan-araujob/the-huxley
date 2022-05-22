n1 = float(input())
n2 = float(input())
n3 = float(input())
freq = float(input())
media = (n1*2 + n2*2 + n3*3)/7
freq = freq * 100
if freq < 75:
    mensagem = 'Aluno reprovado por faltas!'
elif media > 9:
    mensagem = 'Aluno aprovado com louvor!'
elif 6 <= media <= 9:
    mensagem = 'Aluno aprovado!'
elif 3.9 < media < 6:
    mensagem = 'Aluno de recuperação!'
else:
    mensagem = 'Aluno reprovado!'
print('Frequencia: {:.0f}%'.format(freq))
print('Media: {:.1f}'.format(media))
print(mensagem)