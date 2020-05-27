meuCartão = int(input("Digite o numero do cartão de credito: "))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido != 0 and not encontreiMeuCartãoNaLista:
    cartãoLido = int(input("Digite o numero do proximo cartão de credito: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartãoNaLista = True

if encontreiMeuCartãoNaLista:
    print("EBA!! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está la")
