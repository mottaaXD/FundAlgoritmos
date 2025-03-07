while True:
    num = int(input("Digite um número: "))
    if num >= 0 and num <= 10:
        print("Número aceito")
        break
    else:
        print("Erro")