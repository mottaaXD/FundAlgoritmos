a = 5

def alteraValor():
    global a
    a = 7
    print("Dentro da função 'a' vale: ", a)

print("'a' antes da chamda da função: ", a)
alteraValor()
print("'a' depois da chamada da função", a)