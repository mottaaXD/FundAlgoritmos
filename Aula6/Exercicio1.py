q = int(input("Digite a quatidade de números a serem testados: "))
primo = 0
for i in range(q):
    n = int(input(f"Digite o número {i+1}: "))
    if n > 1:
        is_prime = True
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            primo += 1    
print(f"Você digitou {primo} números primos de um total de {q} números")            