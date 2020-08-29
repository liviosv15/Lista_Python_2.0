nome = str(input('Nome: '))
while len(nome) <=3:
    print('Nome inválido!')
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while (idade<0 or idade>150):
    print('Indade inválida!')
    idade = int(input('Idade: '))

salario = float(input('Salário: '))
while (salario<=0):
    print('Salário inválido!')
    salario = float(input('Salário: '))

sexo = str(input('Sexo ("F"/"M"): '))
if (sexo=="M"):
    print('Masculino.')
else:
    print('Feminino')
status = str(input('Estado sivil ("S", "C", "V", "D"): '))
if (status=="S"):
    print('Solteir@.')
else:
    if (status == "C"):
        print('Casad@.')
    else:
        if (status == "V"):
            print('Viuv@.')
        else:
            print('Divorciad@.')