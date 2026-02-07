print('|{}|'.format('*'*31))
print('|     PROGRESSAO ARITMETICA     |')
print('|{}|'.format('*'*31))

n = int(input('Isira o primeiro termo: '))
r = int(input('Isira a razão: '))
cont = 0

while cont < 10:
    print(n, end= ' -> ')
    n+=r
    cont +=1

print ('ACABOU!!!')