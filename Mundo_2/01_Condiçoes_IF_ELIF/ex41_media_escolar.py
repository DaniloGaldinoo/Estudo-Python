# Exercício 41 - Situação do Aluno
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula a média de um aluno
# com base em duas notas e informa se está aprovado,
# em recuperação ou reprovado.

print ('\033[32m' + '*~' * 9 + '\033[m')
print ('\033[34m' + '* ESCOLA GALDINO *' + '\033[m')
print ('\033[32m' + '*~' * 9 + '\033[m')

nome = str(input('Qual o nome do Aluno? --> '))
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insita a segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('ALUNO '+'\033[35m' + 'REPROVADO!' + '\033[m')
elif media >= 5 and media <= 6.9:
    print('ALUNO EM ' + '\033[35m' + 'RECUPERAÇAÕ!' + '\033[m')
else:
    print('ALUNO '+'\033[32m' + 'APROVADO!!!' + '\033[m')
