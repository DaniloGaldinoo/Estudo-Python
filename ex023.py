num = int(input('Insira um numero entre 0 e 9999: '))
if num < 0 or num > 9999:
    print("Numero Invalido!")
else:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
print(f'Analisando o numero {num}\nUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')



# EU TINHA FEITO ASSIM, MAS NA AULA MOSTROU UM MODO MAIS FACIL E COMPLETO

# div = list(str(num))
# print(f"""A separação fica assim:
# Unidade: {div[3]}
# Dezena: {div[2]}
# Centena: {div[1]}
# Milhar: {div[0]}""")