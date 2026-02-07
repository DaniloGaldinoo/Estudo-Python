nome = str(input('Digite o seu nome completo: ')).strip()
#.strip remove os espaços na frente e atras do que o usuario inserir!
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))

a = nome.count(' ')
b = len(nome)
tot = b-a
print ('Seu nome tem um total de {} letras!'.format(tot)    )
#print('Seu nome tem ao todo{} letras'.format(len(nome) - nome.count(' ')))
#Guanabara fez sem a conta em cima, fez tudo na mesma linha, como no comentario acima

div = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(div[0])))