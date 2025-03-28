lista = []
num_par = []
soma_ind_par = 0
for i in range (10):
    numero = int(input("Digite um número: "))
    lista.append(numero)
print(f"Números: {lista}") 
soma = 0   
for num in lista:
    if num % 2 == 0:
        num_par.append(num)
for x in num_par:
    soma += x
print(f"A soma dos números pares é: {soma}")
for indice in range (0, len(lista), 2):
    soma_ind_par += lista[indice]
print(f"Soma elementos indices par: {soma_ind_par}")


