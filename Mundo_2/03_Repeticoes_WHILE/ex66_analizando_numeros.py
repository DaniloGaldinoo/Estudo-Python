# Exercício 66 - Analisando Números
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário inserir vários números
# e calcula a média, o maior e o menor valor digitado.

print ('*'*22)
print ('{:^20}'.format('* ANALISANDO NUMEROS *'))
print ('*'*22)

n = 0
soma = 0
qtdnum = 0
maior = n
menor = n
a = 'S'

while a == 'S':
    n = int(input(f'Insira o {qtdnum + 1}º numero: '))
    qtdnum += 1
    soma += n
    if n > maior:
        maior = n
    else:
        n < menor
        menor = n
    a = str(input('Você deseja inserir mais valores? [S/N] -> ')).upper().strip[0]
media = soma / qtdnum
print (f'A media dos numeros inseridos é: {media:.2f}')
print (f'O maior numero digitado foi {maior}')
print (f'O menor numero digitado foi {menor}')
