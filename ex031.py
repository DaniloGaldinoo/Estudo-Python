print ('-------------------------')
print ('| * CALCULO DA VIAGEM * |')
print ('-------------------------')
km = float(input('Insira quantos kilometros tem a viagem: '))
vlr = 0

if km <= 200:
    vlr = km * 0.50
else:
    vlr = km * 0.45

print(f'O valor da passagem é R$:{vlr:.2f}')