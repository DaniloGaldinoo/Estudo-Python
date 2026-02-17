#Guanabara fez usando parenteses entes d in(input) para solicitar a entrada de dados e fazer uma tupla assim.
#núm = (int(input('Digite um numero: ')),
#       int(input('Digite outro numero: '))) <- Metodo guanabara, eu preferi fazer com outro exemplo usando tuplas vazias.
t = ()
tp = ()
for c in range(1,5):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        tp = tp + (n,)
    t = t + (n,)
print (f'Os numeros digitados foram: {t}')
print (f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print (f'O valor 3 apareceu na posição {t.index(3)+1}')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print (f'Os numeros pares digitados foram: {tp}')
