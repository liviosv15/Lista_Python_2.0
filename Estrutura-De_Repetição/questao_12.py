num = int(input('Informe um número de 1 a 10: '))
i = 1
print('Tabuada de {}:'.format(num))
print("====================")
print('{} X 1 = {}'.format(num, num))
print('____________________')
for i in range(1,10):
    i+=1
    tab = num*i
    print('{} X {} = {}'.format(num, i, tab))
    print('____________________')


