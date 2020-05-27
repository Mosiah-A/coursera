n = int(input("Digite o valor de n: "))
factorial = 1
if n == 0:
    print(1)
else:
    for i in range(1,n + 1):
        factorial = factorial*i
    print(factorial)
