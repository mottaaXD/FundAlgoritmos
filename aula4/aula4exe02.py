valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite um segundo valor: "))
valor3= int(input("Digite um terceiro valor: "))

numeros = [valor1, valor2, valor3]
numeros_ordenados = sorted(numeros, reverse=True)
print(f"Os valores em ordem decrescentes são: {numeros_ordenados}")
