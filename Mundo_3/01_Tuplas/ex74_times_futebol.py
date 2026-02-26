# Exercício 74 - Times de Futebol
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Manipula uma tupla com os 20 times do Brasileirão,
# mostrando os 5 primeiros, os 4 últimos, a ordem alfabética
# e a posição do time Chapecoense.

time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
        'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
        'Fluminense', 'Sport Recife', 'EC Vitoria', 'Curitiba', 'Avaí',
        'Ponte Preta', 'Atlético GO')

print ('-='*20)
print (f'Os times participantes são: {time}')
print ('-='*20)
print (f'Os primeiros 5 colocados são: {time[0:5]}')
print ('-='*20)
print (f'Os ultimos 4 colocados são: {time[-4:]}')
print ('-='*20)
print (f'Ordem alfabetica: {sorted(time)}')
print ('-='*20)
print (f'Chapecoense se encontra na posição: {time.index ('Chapecoense')+1}ª')
