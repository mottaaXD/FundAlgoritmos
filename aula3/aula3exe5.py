anoAtual = int(input("Qual o ano atual?"))
anoNasc = int(input("Qual o ano em que nasceu?"))

idade = anoAtual - anoNasc

if idade >= 18:
    print("Ja pode tirar CNH")
else:
    print("Ainda não pode tirar CNH")    