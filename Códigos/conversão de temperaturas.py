#CONVERSÃO DE TEMPERATURAS
def main():
    print("Qual temperatura você quer converter?\n")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    escolha = int(input(""))
    não_escolha = False
    #fim = True
    if escolha <= 0 or escolha > 4:
        while not não_escolha:
            print("Essa opção não corresponde à nenhuma das opções, por favor, escolha novamente.")
            escolha = int(input(""))
            if escolha >= 1 or escolha <= 4:
                não_escolha = True
    elif escolha == 1:
        print ("A temperatura de Celsius para Fahrenheit é:", C_F())
    elif escolha == 2:
        print ("A temperatura de Fahrenheit para Celsius é:", F_C ())
    elif escolha == 3:
        print ("A temperatura de Celsius para Kelvin é:", C_K ())
    else:
        print ("A temperatura de Kelvin para Celsius é:", K_C ())

def C_F ():
    C = int(input("Qual a temperatura em Celsius? "))
    F = 1.8*C + 32
    return F

def F_C ():
    F = int(input("Qual a temperatura em Fahrenheit? "))
    C = 5*((F - 32)/9)
    return C

def C_K ():
    C = int(input("Qual a temperatura em Celsius? "))
    K = C + 273
    return K

def K_C ():
    K = int(input("Qual a temperatura em Kelvin? "))
    C = K - 273
    return C

inicio = main()
