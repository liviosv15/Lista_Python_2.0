a = int(input('Informe um número inteiro: '))
b = int(input('Informe um número inteiro: '))
c = int(input('Informe um número inteiro: '))

if (a>b and b>c and a>c):
    print(a, b, c)
else:
    if (b>a and b>c and c>a):
        print(b, c, a)
    else:
        if (c>a and c>b and a>b):
            print(c, a, b)
        else:
            if (b>a and b<c and c>a):
                print (c, b, a)