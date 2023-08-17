ganho_hora = int(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quanto você trabalha por mês? "))
salario_bruto = ganho_hora*horas_mes
IR = (salario_bruto*11)/100
salario_descontado = salario_bruto - IR
INSS = (salario_descontado*8)/100
salario_descontado = salario_descontado - INSS
sindicato = (salario_descontado*5)/100
salario_liquido = salario_descontado - sindicato
print (f'+ Salário Bruto: {salario_bruto:.2f} R$')
print (f'- IR (11%): {IR:.2f} R$')
print (f'- INSS (8%): {INSS:.2f} R$')
print (f'- Sindicato (5%): {sindicato:.2f} R$')
print (f'= Salário Líquido: {salario_liquido:.2f} R$')

