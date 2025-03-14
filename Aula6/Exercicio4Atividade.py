valor = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))
if parcelas == 1:
    if valor > 5000:
        desconto =valor*(10/100)
        descontoEx = valor*(5/100)
        descontoF = desconto + descontoEx
        valorF = valor - descontoF
        valorP = valorF/parcelas
        print(f"Desconto total: {descontoF:.2f}")
        print(f"Valor final da compra com desconto: {valorF:.2f}")
        print(f"Cada parcela será de: {valorP:.2f}")
    else:
        desconto =valor*(10/100)
        valorF = valor - desconto
        valorP = valorF/parcelas
        print(f"Desconto total: {desconto:.2f}")
        print(f"Valor final da compra com desconto: {valorF:.2f}")
        print(f"Cada parcela será de: {valorP:.2f}")
elif parcelas == 2 or parcelas == 3:
        if valor > 5000:
            desconto =valor*(5/100)
            descontoEx = valor*(5/100)
            descontoF = desconto + descontoEx
            valorF = valor - descontoF
            valorP = valorF/parcelas
            print(f"Desconto total: {descontoF:.2f}")
            print(f"Valor final da compra com desconto: {valorF:.2f}")
            print(f"Cada parcela será de: {valorP:.2f}")
        else:
            desconto =valor*(5/100)
            valorF = valor - desconto
            valorP = valorF/parcelas
            print(f"Desconto total: {desconto:.2f}")
            print(f"Valor final da compra com desconto: {valorF:.2f}")
            print(f"Cada parcela será de: {valorP:.2f}")
else:
    if valor > 5000:
        descontoEx = valor*(5/100)
        valorF = valor - descontoEx
        valorP = valorF/parcelas
        print(f"Desconto total: {descontoEx:.2f}")
        print(f"Valor final da compra com desconto: {valorF:.2f}")
        print(f"Cada parcela será de: {valorP:.2f}")
