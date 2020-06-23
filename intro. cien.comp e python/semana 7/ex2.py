'''L = int(input("Digite a largura: "))
A = int(input("Digite a altura: "))

c =1
linha = 1

while linha <= A:
    while c <= L:
        
        if linha == 1 or c == 1:
            print("#", end="")             
        if linha == L or c == L:
            print("#", end = "")
        c += 1
    #print('#', end = "")
    linha += 1
    print()
    c = 1'''

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
caractere = "#"
print(caractere * largura) # cabeçalho

for i in range(altura-2):
    espacos = (largura - 2) * ' '
    print("%s%s%s" % (caractere, espacos, caractere)) # meio

print(caractere * largura) # rodapé
