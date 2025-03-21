def funcao(n1, n2, n3):
    calc = (n1**0.5)+(n2**0.5)+(n3**0.5)+(n1+n2)/2+(n2+n3)/2+(n1+n3)/2
    return calc

num1 = int(input("N1 "))
num2 = int(input("N2 "))
num3 = int(input("N3 "))

print(funcao(num1, num2 , num3))