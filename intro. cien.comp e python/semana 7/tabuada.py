#Taboada
linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end ="\t") # \t divide cada linha em espaço multiplo de 8
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1
