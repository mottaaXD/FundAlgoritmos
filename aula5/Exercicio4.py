maior = -9999999
x = 0
while x < 6:
    nro=int(input("Digite um número: "))
    if nro>maior:
        maior = nro
    x = x+1
print("O maior é:", maior)        