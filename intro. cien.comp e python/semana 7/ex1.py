L = int(input("Digite a largura: "))
A = int(input("Digite a altura: "))

c =1
d = 1
while d <= A:
    while c <= L:
        c += 1
        print("#", end="")
    d += 1
    print()
    c = 1

