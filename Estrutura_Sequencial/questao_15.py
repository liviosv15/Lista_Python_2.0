th = float(input('Quanto vc ganha por hora? '))
hora = float(input('Quantas horas vc trabalha por mês? '))
sb = th*hora
ir = sb*0.11
inss = (sb-ir)*0.08
sindicato = (sb-ir-inss)*0.05
print('Salário Bruto: R$',sb)
print ('Imposto de Renda (11%): R$',ir)
print('INSS (8%): R$', inss)
print('Sindicato (5%): R$',sindicato)
sliquido = sb-ir-inss-sindicato
print('Salário Líquido R$',sliquido)