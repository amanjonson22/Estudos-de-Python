#Loja de Tintas - Escolhendo qual lata comprar de acordo com o tamanho do local a ser pintado
tamanho_pintar = int(input("Qual o tamanho em metros quadrados a ser pintado? "))
quantidade_litros_pintar = tamanho_pintar/6
print(f'\nA quantidade de litros necessários para pintar: {quantidade_litros_pintar:.1f}L')
lata1 = 18
preço_lata1 = 80
lata2 = 3.6
preço_lata2 = 25 

#SITUAÇÃO 1 - APENAS COMPRAR LATAS DE 18L
quantidade_latas1_float = quantidade_litros_pintar/lata1

if float(quantidade_latas1_float) > int(quantidade_latas1_float):
    quantidade_latas1_int = int(quantidade_latas1_float)+1

sobra_lata1 = quantidade_latas1_int - quantidade_latas1_float

preço_total_lata1 = quantidade_latas1_int*preço_lata1

print("\nSituação 1: Apenas comprar latas de 18L, que valem 80 reais")
print(f'quantidade de latas 2: {quantidade_latas1_int:.0f}; \nsobra: {sobra_lata1:.1f}L; \npreço total: R${preço_total_lata1:.2f}')


#SITUAÇÃO 2 - APENAS COMPRAR LATAS DE 3.6L
quantidade_latas2_float = quantidade_litros_pintar/lata2

if float(quantidade_latas2_float) > int(quantidade_latas2_float):
    quantidade_latas2_int = int(quantidade_latas2_float)+1
    
sobra_lata2 = quantidade_latas2_int - quantidade_latas2_float

preço_total_lata2 = quantidade_latas2_int*preço_lata2

print("\nSituação 2: Apenas comprar latas de 3,6L, que valem 25 reais")
print(f'quantidade de latas 2: {quantidade_latas2_int:.0f}; \nsobra: {sobra_lata2:.1f}L; \npreço total: R${preço_total_lata2:.2f}')


#SITUAÇÃO 3 - COMPRAR MISTURADO, TANTO LATAS DE 18L QUANTO DE 3.6L PARA DESPERDIÇAR MENOS. ACRESCENTANDO 10% DE FOLGA.
quantidades_litros_falta_pintar = quantidade_litros_pintar + ((quantidade_litros_pintar*10)/100)
while quantidades_litros_falta_pintar > 18:
    quantidade_latas1_sit3_int = quantidade_litros_pintar//lata1
    quantidades_litros_falta_pintar = quantidades_litros_falta_pintar - (quantidade_latas1_sit3_int*lata1)

valor_lata1 = quantidade_latas1_sit3_int * preço_lata1

quantidade_latas2_sit3_float = quantidades_litros_falta_pintar/lata2
if float(quantidade_latas2_sit3_float) > int(quantidade_latas2_sit3_float):
    quantidade_latas2_sit3_int = int(quantidade_latas2_sit3_float)+1

sobra_lata2_sit3 = quantidade_latas2_sit3_int - quantidade_latas2_sit3_float

valor_lata2 = quantidade_latas2_sit3_int * preço_lata2

valor_total_sit3 = valor_lata1 + valor_lata2

print("\nSituação 3: Comprar misturado, tanto latas de 18L, que valem R$80, quanto de 3.6L, que valem R$25. \nAcrescentando 10% de folga\n")
print(f'quantidade de latas 1: {quantidade_latas1_sit3_int:.0f};\nquantidade de latas 2: {quantidade_latas2_sit3_int:.0f};\nsobra: {sobra_lata2_sit3:.1f}L; \npreço total: R${valor_total_sit3:.2f}')
