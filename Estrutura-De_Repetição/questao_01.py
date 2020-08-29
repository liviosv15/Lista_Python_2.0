num = int(input('Informe uma nota entre 0 e 10: '))
while (num<0 or num>10):
    print('Inválido.')
    num = int(input('Informe novamente: '))
print('Válido.')