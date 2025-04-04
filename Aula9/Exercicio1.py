lista = []

x = True
while x == True:
    numeros = int(input("Digite um número"))
    lista.append(numeros)
    if numeros < 0:
        break

def lista1(num):
    return num >= 0 and num <=25

lista1_f = filter(lista1, lista)
print("Entre 0 e 25: ", list(lista1_f))


def lista2(num):
    return num >= 26 and num <=50

lista2_f = filter(lista2, lista)
print("Entre 26 e 50: ", list(lista2_f))

def lista3(num):
    return num >= 51 and num <=75

lista3_f = filter(lista3, lista)
print("Entre 51 e 75: ", list(lista3_f))

def lista4(num):
    return num >= 76 and num <=100

lista4_f = filter(lista4, lista)
print("Entre 76 e 100: ", list(lista4_f))