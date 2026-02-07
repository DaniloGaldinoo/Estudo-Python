print('|*****************************|')
print('|  *  FORMAÇÃO TRIANGULAR  *  |')
print('|*****************************|')
a = float(input('Insira o valor da primeira reta: '))
b = float(input('Insira o valor da segunda reta: '))
c = float(input('Insira o valor da terceira reta: '))

while True:

    if a < b+c and b < a+c and c < a+b:
        print('Esses valores FORMAM UM TRIANGULO!')

        if a == b and b == c:
            print('TRATA-SE DE UM TRIANGULO EQUILATERO!')
        elif a == b and b != c:
            print('TRATA-SE DE UM TRIANGULO ISÓSCELES!')
        elif a != b and b != c:
            print('TRATA-SE DE UM TRIANGULO ESCALENO!')
    else:
        print('NÃO FORMAM UM TRIANGULO')
    break