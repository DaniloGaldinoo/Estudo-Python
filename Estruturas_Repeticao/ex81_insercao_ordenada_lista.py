# Exercício 81 - Inserção Ordenada em Lista
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário digitar 5 valores, que são
# inseridos em uma lista já ordenada de forma crescente.
# Exibe a posição onde cada novo valor foi adicionado e,
# ao final, mostra a lista completa em ordem.

lista = []

for cont in range (5):
    n = int(input('Digite um Valor: '))

    if len(lista) == 0:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista) and n >lista[pos]:
            pos+=1
        lista.insert(pos, n)
        print(f'Adicionado na posição {pos} da lista...')


print (f'Os valores digitados em ordem foram {lista}')
