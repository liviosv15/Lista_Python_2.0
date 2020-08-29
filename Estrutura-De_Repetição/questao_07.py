num = 0
n = 1

while n<=5:
    num1 = int(input('Informe um número: '))
    if num1 > num:
        num = num1
    n += 1
print('O maior é: ', num)