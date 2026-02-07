from time import sleep

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
print ('\nPAUSA')

while True:
    resp = int(input('\nQuantos termos a mais você quer ver? [0 para sair] -> '))

    if resp == 0:
        print ('S A I N D O . . .')
        sleep(0.4)
        break
    cont2 = 0
    while cont2< resp:
        print(n, end= ' -> ')
        n+=r
        cont2 += 1
print ('\nFIM')