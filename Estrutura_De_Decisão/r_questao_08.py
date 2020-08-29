ype = float(input('Inofrme o preço do Ypê: '))
limpol = float(input('Inoforme o preço do Limpol: '))
minuano = float(input('Informe o preço do Minuano: '))

if (ype >= limpol):
    print('Você vai levar o Limpol')
else:
    if (limpol <= minuano):
        print('Você vai levar o Minuano')
    else:
        print('Você vai levar o Ypê')