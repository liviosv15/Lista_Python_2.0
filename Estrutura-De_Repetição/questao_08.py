num = 0
n = 1
num2 = 0
while n<=5:
    num1 = int(input('Informe um número: '))
    num2 = (num2+num1)
    n+=1
media = num2/5
print('Soma: {} e a Média: {}'.format(num2, media))