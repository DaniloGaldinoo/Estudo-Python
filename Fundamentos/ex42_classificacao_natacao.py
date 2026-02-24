# Exercício 42 - Classificação de Atleta
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que classifica um atleta
# de acordo com sua idade na categoria
# da Confederação Nacional de Natação.

print ('\033[32m' + '=-' * 18 + '\033[m')
print ('\033[34m' + '* CONFEDERAÇÃO NACIONAL DE NATAÇÃO *' + '\033[m')
print ('\033[32m' + '=-' * 18 + '\033[m')

nasc = int(input('Insira o ano de nascimento: '))
idade = 2025 - nasc

if idade <= 9:
    print('CATEGORIA MIRIM!')
elif idade >= 10 and idade <= 14:
    print('CATEGORIA INFANTIL!')
elif idade >= 15 and idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade == 20:
    print('CATEGORIA SENIOR!')
else:
    print('CATEGORIA MASTER!')