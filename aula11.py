print('\033[1;31;40mOla, Mundo!\033[m')


a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')

#também da para fazer usando o format nas cores.

print('Os valores são {}{}{} e {}{}{}'.format('\033[4;31m', a, '\033[m', '\033[4;32m', b,'\033[m'))

#ou no f' novo

print(f'Os valores são \033[1;35m{a}\033[m e \033[1;33m{b}\033[m')

#Da para criar uma lista de cores adicionando o codigo como uma variavel!
##Por exemplo->

cores = {'limpa':'\033[m', 'azul':'\033[36m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;40m'}
nome = 'Dan'
print (f'Olá! Muito prazer em te conhecer, {(cores['pretoebranco'])}{nome}{(cores['limpa'])}!!')