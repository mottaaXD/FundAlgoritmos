def calc(dividendo, divisor):
    quociente = 0
    resto = dividendo

    while resto >=divisor:
        resto-= divisor
        quociente +=1
    return quociente, resto

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente, resto = calc(dividendo, divisor)
print(f"O quociente é: {quociente}")
print(f"O resto é: {resto}")    