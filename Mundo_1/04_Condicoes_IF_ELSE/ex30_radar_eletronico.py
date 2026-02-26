# Exercício 30 - Radar Eletrônico
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica a velocidade de um veículo
# e calcula o valor da multa caso ultrapasse 80 km/h.

print ('---------------------')
print ('|  *  R A D A R  *  |')
print ('---------------------')
km = float(input('Quantos km/h atingiu? '))
multa = 0
exced = km - 80

if km > 80.0:
    print('Você foi MULTADO!')
    print(f'Você estava a {exced} km acima do limite permitido.')
    print(f'Sua multa é de R$:{exced*7}')
else:
    print('VELOCIDADE PERMITIDA!')