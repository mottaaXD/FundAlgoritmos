lista = []
for x in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)
print(lista)
print("Elementos maiores que a soma de dois antecessores:")
for i in range(2, len(lista)):
    if lista[i] > lista[i-1] + lista[i-2]:
        print(lista[i])