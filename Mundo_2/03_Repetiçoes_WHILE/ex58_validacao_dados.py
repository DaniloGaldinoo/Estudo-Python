# Exercício 58 - Validação de Dados
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Lê o sexo informado pelo usuário
# e continua solicitando até que uma opção válida
# seja digitada.

resp = 'S'

while resp == 'S':
    sexo = str(input('Insira o sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        print('O sexo informado foi MASCULINO!')
    elif sexo == 'F':
        print ('O sexo informado foi FEMININO!')
    else:
        print ('ENTRADA INVALIDA, Tente novamente')
    resp = str(input('Deseja continuar? [S/N]: ')).upper()