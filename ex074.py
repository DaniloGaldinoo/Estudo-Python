from random import randint
aleat = tuple((randint(1,10) for c in range(1, 6)))

print (f'Os valores sorteados foram: {aleat}')
print (f'O maior valor sorteado foi: {max(aleat)}')
print (f'O menor valor sorteado foi: {min(aleat)}')
