print('|{}|'.format('*'*24))
print('|     NUMEROS PRIMOS     |')
print('|{}|'.format('*'*24))

n = int(input('Insira o numero que deseja saber: '))
cont = 0

for c in range (1, n+1):
    if n % c == 0:
        cont += 1

if cont == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')