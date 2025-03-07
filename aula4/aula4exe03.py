altura = float(input("Qual é a sua altura?"))
sexo = int(input('''Qual é o seu sexo?
Homem=0
Mulher=1          '''))

if sexo==0:
    pesoIdeal = (72.7 * altura) -58
    print(f"Seu peso ideal é: {pesoIdeal}")
elif sexo==1:
    pesoIdeal = (62,1 * altura) - 44.7
    print(f"Seu peso ideal é: {pesoIdeal}")
else:
    print("Erro")    
