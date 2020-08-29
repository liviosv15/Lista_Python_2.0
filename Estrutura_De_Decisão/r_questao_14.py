nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1+nota2)/2

if (media>=9.0 and media<=10.0):
    print('Suas notas foram: {} e {}, Sua média final: {}, média de aproveitamento: A.'.format(nota1, nota2, media))
    print('Você foi APROVADO!')
else:
    if (media>=7.5 and media<=9.0):
        print('Suas notas foram: {} e {}, Sua média final: {}, média de aproveitamento: B.'.format(nota1, nota2, media))
        print('Você foi APROVADO!')
    else:
        if (media>=6.0 and media<=7.5):
            print('Suas notas foram: {} e {}, Sua média final: {}, média de aproveitamento: C.'.format(nota1, nota2, media))
            print('Você foi APROVADO!')
        else:
            if (media>=4.0 and media<=6.0):
                print('Suas notas foram: {} e {}, Sua média final: {}, média de aproveitamento: E.'.format(nota1, nota2, media))
                print('Você foi REPROVADO!')
            else:
                print('Suas notas foram: {} e {}, Sua média final: {}, média de aproveitamento: D.'.format(nota1, nota2, media))
                print('Você foi REPROVADO!')
