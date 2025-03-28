qntd = int(input("Digite a quantidade de números: "))
numeros = []

for i in range(qntd):
    num = int(input("Digite um número: "))
    numeros.append(num)

numerosInv = sorted(numeros, reverse=True)
print(f"Números: {numeros}")
print(f"Inverso: {numeros[::-1]}")    