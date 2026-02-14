t = ()
tp = ()
cont = 1
cnove = 0
posi = 0
pinicial = 0
par = 0

for c in range(1,5):
    n = int(input(f'Digite o {c}º valor: '))
    if n == 9:
        cnove += 1
    if n == 3 and posi == 0:
        posi = cont
    if n % 2 == 0:
        tp = tp + (n,)
    t = t + (n,)
    cont+=1
if cnove != 0:
    print (f'O numero 9 aparece {cnove} vezes')
else:
    print ('O numero 9 não foi digitado; Sendo assim, aparece 0 vezes')
if posi != 0:
    print (f'O numero 3 foi digitado na posição {posi}')
else:
    print ('O numero 3 não foi digitado nenhuma vez; então não esta em nenhuma posição!')
print (f'Os numeros pares digitados foram: {tp}')
