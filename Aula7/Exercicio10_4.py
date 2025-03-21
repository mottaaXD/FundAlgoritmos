multiplo = lambda x, y: x % y

num1 = int(input("NUM1 "))
num2 = int(input("NUM2 "))

if multiplo(num1, num2) == 0:
    print("É multiplo")
else:
    print("Não é multiplo")    