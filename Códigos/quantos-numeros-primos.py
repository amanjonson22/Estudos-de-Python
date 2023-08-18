def n_primos(n):
    quantidade_primos = 1
    numero_primo = 2
    n_divide = 2
    quantidade_primos_novo = quantidade_primos
    quantidade_divisões = 0
    resto = 1
    if n == 2:
        quantidade_primos = 1
        return quantidade_primos
    else:
        while numero_primo <= n:
            while numero_primo >= n_divide:
                resto = numero_primo % n_divide 
                quantidade_divisões +=1
                if resto != 0 and quantidade_divisões == numero_primo//2 and numero_primo != 2:
                    quantidade_primos_novo = quantidade_primos + 1
                    if quantidade_primos_novo != quantidade_primos:
                        n_divide = numero_primo + 1
                elif resto == 0:
                    n_divide = numero_primo + 1
                else:
                    n_divide += 1
            numero_primo += 1
            n_divide = 2
            quantidade_primos = quantidade_primos_novo
            quantidade_divisões = 0
    return quantidade_primos
