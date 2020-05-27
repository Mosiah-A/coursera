'''while condição:
    comando1
    comando2
comandoFinal

i = 0
while i <= 10:
    print(2**1)
    i = i + 1'''

decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente == True:
    print("A sequência está em ordem decrescente!")
else:
    print("A sequencia não é em ordem decrescente!")
