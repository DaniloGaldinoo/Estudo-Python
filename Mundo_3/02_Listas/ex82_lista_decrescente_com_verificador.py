# Exercício 82 - Lista Decrescente com verificador
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuario inserir quantos valores desejar e analisa se existe o numero 5 ou nao;
# e apresenta a listagem de forma decrescente

lista = []
qtnum = 0

while True:
    n = int(input('Insira um valor: '))
    qtnum += 1
    lista.append(n)

    while True:
        sair = input('Deseja Continuar? [S/N] -> ').strip().upper()
        if sair in ['S', 'N']:
            break
        else:
            print('INVALIDO! Insira [S/N]')

    if sair == 'N':
        break

print (f'Você digitou {qtnum} elementos.')
lista.sort(reverse=True)
print (f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 esta na lista!')
else:
    print('O valor 5 NÃO esta na lista!')