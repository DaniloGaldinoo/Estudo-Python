"""
Exercício 80 - Valores Únicos em Lista
Curso: Python
Autor: Danilo Galdino
Descrição: Permite ao usuário digitar vários valores,
não adicionando duplicados, e exibe a lista final em ordem crescente.
"""

valores = []

while True:
    num = int(input('Digite um Valor: '))

    if num in valores:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor Adicionado com sucesso...')

    while True:
        sair = input('Quer continuar? [S/N] ').upper()
        if sair in ['S', 'N']:
            break
        else:
            print('INVÁLIDO. Insira [S/N]')

    if sair == 'N':
        break

print('-='*20)
print(f'Você digitou os valores: {sorted(valores)}')