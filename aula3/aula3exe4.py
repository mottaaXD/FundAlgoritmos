salario = int(input("Qual é o seu salário?"))

if salario > 1250:
    novo_salario =  salario + (salario * (10/100))
    print(f"Recebeu 10% de aumento, seu salario agora é: R$%{novo_salario:.2f}")
if salario <= 1250:
    novo_salario =  salario + (salario * (15/100))
    
    print(f"Recebeu 15% de aumento, seu salario agora é: R${novo_salario:.2f}")    