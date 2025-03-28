num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
num3 = float(input("Digite um número: "))
num4 = float(input("Digite um número: "))
num5 = float(input("Digite um número: "))
num6 = float(input("Digite um número: "))
num7 = float(input("Digite um número: "))
num8 = float(input("Digite um número: "))
num9 = float(input("Digite um número: "))
num10 = float(input("Digite um número: "))

lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
listaOr = sorted(lista)
print(f"Números: {lista}")
for indice in range(len(lista)):
    if lista[indice] == listaOr[9]:
        print(f"Maior número: {listaOr[9]}")
        print(f"Indice do maior número: {indice}")
        break
