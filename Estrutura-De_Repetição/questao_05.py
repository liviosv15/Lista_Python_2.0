print('OBS: Informe primeiro a quantidade de habiantes do menor páis!!')
a = int(input('Quantidade de habitantes do país A: '))
ta = float(input('Taxa anual de crescimento: '))
b = int(input('Quantidade de habitantes do país B: '))
tb = float(input('Taxa anual de crescimento: '))
ano = 1
ta=ta/100
tb=tb/100

while (a<b):
    a = a+(a*ta)
    b = b+(b*tb)
    ano = ano+1
print('{} anos para que se iguale o nº de habitantes.'.format(ano))