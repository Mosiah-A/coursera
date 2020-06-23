n = int(input("Digite um número inteiro >1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print ("fator ", fator, "multiplicidade = ", multiplicidade)
        cont = 0
        for c in range (1, fator+1):
            if fator % c == 0:
                cont += 1           
        if cont == 2:
            print('O numero {} é primo'.format(fator))
        else:
            print('O numero {} não é primo'.format(fator))
    fator = fator + 1
    multiplicidade = 0
