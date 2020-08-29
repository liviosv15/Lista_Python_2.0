n1 = float(input('Iforme a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
nota = (n1+n2)/2

if (nota == 10):
    print('Aprovado com Distinção, nota: ', nota)
else:
    if (nota >= 7):
        print('Aprovado, nota: ', nota)
    else:
        print('Reprovado, nota: ', nota)
