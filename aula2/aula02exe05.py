porHora = float(input("Quanto você ganha por hora?"))
horasPorMes = float(input("Quantas horas por mês?"))
salario = porHora * horasPorMes
ir = salario *(11/100)
inss = salario *(8/100)
sindicato = salario * (5/100)
salarioLiquido = salario - ir - inss - sindicato

print("O salario bruto é:", salario)
print("O valor do ir é:", ir)
print("O valor do inss é:", inss)
print("O valor do sindicato é:", sindicato)
print("O salario liquido é:", salarioLiquido)
