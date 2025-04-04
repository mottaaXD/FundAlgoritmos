#Exemplo filtrando numeros pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

#Modo tradicional
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

#Usando list comprehension
numeros_pares_compr = [numero for numero in numeros if numero % 2 == 0]

print(numeros_pares)
print(numeros_pares_compr)