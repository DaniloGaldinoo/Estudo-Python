n1 = int(input('Insira o numero que quer ver a tabuada: '))
print('|{}|'.format('*'*23))
print('|     T A B U A D A     |')
print('|{}|'.format('*'*23))

for c in range (1, 11):
    print(f'|    {c:2} x {n1:2} = {c*n1:2}       |')

print('|{}|'.format('*'*23))