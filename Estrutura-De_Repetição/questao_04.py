a = 80000
b = 200000
ano = 1

while (a<b):
    a = a+(a*0.03)
    b = b+(b*0.015)
    ano = ano+1
print('Vai pecisar de {} anos até que o país A se iguale ao país B.'.format(ano))