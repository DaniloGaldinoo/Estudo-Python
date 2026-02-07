print ('*'*26)
print ('{:^22}'.format('*    CAIXA ELETRONICO    *'))
print ('*'*26)
cinq = vin = dez = um = 0

valor = int(input('Que valor voce quer sacar? R$: '))

while valor >= 50:
    valor = valor - 50
    cinq += 1
while valor >= 20:
    valor = valor - 20
    vin += 1
while valor >= 10:
    valor = valor - 10
    dez += 1
while valor >= 1:
    valor = valor - 1
    um += 1

print (f'Total de {cinq} cedulas de R$50')
print (f'Total de {vin} cedulas de R$20')
print (f'Total de {dez} cedulas de R$10')
print (f'Total de {um} cedulas de R$1')
print('='*28)
print('OBRIGADO, VOLTE SEMPRE!')

