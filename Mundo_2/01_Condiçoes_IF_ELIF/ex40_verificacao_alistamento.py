# Exercício 40 - Verificação de Alistamento Militar
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula a idade do usuário
# com base no ano de nascimento e informa se já passou,
# está no ano ou ainda irá se alistar.

print ('\033[32m' + '*-' * 14 + '\033[m')
print ('\033[34m' + '* VERIFICAÇÃO ALISTAMENTO! *' + '\033[m')
print ('\033[32m' + '*-' * 14 + '\033[m')

ano = int(input('Insira o ano de nascimento: '))
idade = 2025 - ano
passou = idade - 18
idcont = idade
cont = 0
while idcont < 18:
    cont = cont + 1
    idcont = idcont + 1


if idade < 18:
    print (f'Sua idade é {idade} anos, ainda faltam {cont} anos para você se apresentar ao alistamento!')
elif idade > 18:
    print (f'Sua idade é {idade} anos e você esta atrasado com seu alistamento em {passou} anos!')
else:
    print (f'Voce ja tem {idade} anos! Esta no ano do seu alistamento!')