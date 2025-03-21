def funcao(base, altura):
    return(base*altura)/2

while(True):
    b = int(input("Informa a base: "))
    a = int(input("Informe a altura: "))
    print("Area do triangulo: ", funcao(b, a))

    continua = input("Quer calcular a área de mais um triangulo? s/n")

    if continua != "s":
        break