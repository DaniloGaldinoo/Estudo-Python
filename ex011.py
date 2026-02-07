print('Quantos m² minha tinta consegue pintar?')
a = float(input('Insira a altura da parede: '))
l = float(input('Insira a largura da parede: '))
area = a*l
tinta = area/2
print('A quantidade de m² que conseguirá pintar com essa quantidade de tinta é {:.2f}m²\nE serão necessarios {:.2f} litros de tinta'.format(area, tinta))