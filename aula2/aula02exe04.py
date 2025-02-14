dia = int(input("Quantos dias?"))
horas = int(input("Quantas horas?"))
min = int(input("Quantos minutos?"))
sec = int(input("Quantos segundos?"))
tempo = (dia * 24 * 60 * 60) + (horas * 60 * 60) + (min * 60) + sec

print("O tempo total é:", tempo)