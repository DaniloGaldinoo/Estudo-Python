import random

print ('*'*45)
print ('| SORTEIO PARA SABER QUEM APAGARÁ O QUADRO! |')
print ('*'*45)
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
sorteio = random.choice([a1, a2, a3, a4])
print (f'O aluno escolhido foi: {sorteio}')