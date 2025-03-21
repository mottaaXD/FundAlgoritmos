def funcao(num1, num2, num3, num4):
    global numeros
    numeros = [num2, num3, num4]
    if num1 == 1:
        global crescente
        crescente = sorted(numeros)
        print(crescente)
    elif num1 == 2:
        global decrescente
        decrescente = sorted(numeros, reverse=True)   
        print(decrescente)
    elif num1 == 3:
        global maior
        maior = max(numeros)  
        if maior == num2:
            print(num3, maior, num4)
        elif maior == num3:
            print(num2, maior, num4)
        elif maior == num4:
            print(num2, maior, num3)         
    else:
        print("ERROR")
        print("O NUMERO INTEIRO NÃO É VALIDO")
        quit    


i = int(input("Numero inteiro de 1 a 3: "))
a = float(input("Digite um número real: "))
b = float(input("Digite um número real: "))
c = float(input("Digite um número real: "))

funcao(i, a, b, c)