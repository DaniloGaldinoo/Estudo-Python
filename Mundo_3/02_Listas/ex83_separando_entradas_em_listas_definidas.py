# Exercício 83 - Separando entradas em listas pares e impares
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Apresenta 3 listas, uma com todos os valores e outras duas separando os pares dos impares

lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

    while True:
        sair = input('Deseja sair? [S/N] -> ').strip().upper()
        if sair in ['S', 'N']:
            break
        else:
            print('Invalido. Tente novamente.')

    if sair == 'S':
        break

lista.sort()
listapar.sort()
listaimpar.sort()

print (f'Lista completa: {lista}')
print (f'Lista de Pares: {listapar}')
print (f'Lista de Impares : {listaimpar}')


"""Guanabara fez de outra forma mais simplificada!
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um Numero: ')))
    resp = str(input(Quer continuar? [S/N] '
    if resp in 'Nn':
        break
for i, v in enumerate(num)
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)
        
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
"""