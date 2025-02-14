perHour = float(input("Quanto você recebe por hora?"))
hoursPerMonth = int(input("Quantas horas por Mês?"))
salary = perHour * hoursPerMonth
ir = salary * (11/100)
inss = salary * (8/100)
sindicato = salary * (5/100)
salaryLiquido = salary - ir - inss - sindicato
print("Seu salario bruto é:", salary)
print("O valor do IR é:", ir)
print("O valor do INSS é:", inss)
print("O valor do sindicato é:", sindicato)
print("Seu salario líquido é:", salaryLiquido)