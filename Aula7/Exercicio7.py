def funcaoH():
    peso = float(input("Quantos quilos você pesa?"))
    if peso >= 60:
        print("Você está apto a doar sangue")
    else:
        print("Não está apto a doar sangue")
    return
def funcaoM(peso):
    peso = float(input("Quantos quilos você pesa?")) 
    if peso >= 50:
        print("Você está apto a doar sangue")
    else:
        print("Não está apto a doar sangue")
    return

s = input("Homem ou mulher? H/M ")

if s == "h":
    funcaoH()
elif s =="m":
    funcaoM()