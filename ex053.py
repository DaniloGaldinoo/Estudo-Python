print('°{}°'.format('°'*35))
print('°     IDENTIFICANDO PALÍNDROMOS     °')
print('°{}°'.format('°'*35))

fr = str(input('Insira a frase: ')).strip()
frmin = fr.lower()
frjunta = frmin.replace(' ', '')
invertida = ''

for c in range (len(frjunta) -1, -1, -1):
    invertida += frjunta[c]

if frjunta == invertida:
    print(f'O inverso de {frjunta} é {invertida}!\nA frase É um palindromo!')
else:
    print(f'O inverso de {frjunta} é {invertida}!\nA frase NÃO é um palindromo!')
