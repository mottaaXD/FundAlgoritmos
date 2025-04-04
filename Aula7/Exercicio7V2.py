def podeDoar(genero, peso):
    if (genero == "F" and peso >=50) or (genero == "M" and peso >= 60):
        return True
    else:
        return False
    
g = input("Informe o genero (F / M): ")
p = int(input("informe o peso: "))

if podeDoar(g, p):
    print("Pode doar sangue!")
else:
    print("Não pode doar sangue!")    