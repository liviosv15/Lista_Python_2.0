salario = float(input('Informe o seu salário: R$'))
if (salario == 280.00):
    aum = salario*0.20
    total = salario+aum
    print('Salário {}, o aumento é de{}, o total é {}'.format(salario, aum, total))
else:
    if (salario>280.00 and salario<701.00):
        aum = salario*0.15
        total = salario+aum
        print('Salário {}, o aumento é de {}, o total é {}'.format(salario, aum, total))
    else:
        if (salario>700.00 and salario<1501.00):
            aum = salario*0.10
            total = salario+aum
            print('Salário {}, o aumento é de {}, o total é {}'.format(salario, aum, total))
        else:
            if (salario>1500.00):
                aum = salario*0.05
                total = salario+aum
                print('Salário {}, o aumento é de {}, o total é {}'.format(salario, aum, total))