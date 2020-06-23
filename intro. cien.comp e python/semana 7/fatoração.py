def fatoração (n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)

#---------------------------------------#

n = int(input("digite um numero inteiro positivo: "))
while n >= 0:
    fatoração(n)
    n = int(input("digite um numero positivo: "))
