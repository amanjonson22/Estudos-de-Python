tamanho_pintar = int(input("Qual o tamanho em metros quadrados a ser pintado? "))
quantidade_litros_pintar = tamanho_pintar/3
print("A quantidade de Litros necessárias para pintar:", quantidade_litros_pintar)
lata = 18
preço_lata = 80
quantidade_latas_float = quantidade_litros_pintar/lata
if float(quantidade_latas_float) > int(quantidade_latas_float):
    quantidade_latas_int = int(quantidade_latas_float)+1
sobra = quantidade_latas_int - quantidade_latas_float
preço_total = quantidade_latas_int*preço_lata
print(f'A quantidade de latas necessárias é: {quantidade_latas_int:.0f} ; tendo sobra de {sobra:.1f}L e preço total é: R${preço_total:.2f}')
