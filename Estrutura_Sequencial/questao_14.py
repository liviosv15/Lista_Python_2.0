peso = float(input('Kg da pesca de hoje: '))
if (peso > 50):
    exesso = peso-50
    multa = exesso*4
    print('O exesso foi de {:.2f} e a multa é de R${:.2f}'.format(exesso, multa))
else:
    print('A qauntidade de kg não ultrapassou o limite.')