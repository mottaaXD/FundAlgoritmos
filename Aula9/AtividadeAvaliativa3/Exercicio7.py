
x = True
numerosN = []
numerosP = [ ]
while x == True:
    num = int(input(""))
    if num == 0:
        break
    elif num < 0:
        numerosN.append(num)
    elif num >= 0:
        numerosP.append(num)
 
print(numerosN+numerosP)   
