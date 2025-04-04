produto = int(input("Digite o código do produto:"))
quant = int(input("Digite a quantidade do produto:"))
if produto == 1:
    preco = 6.00
    precoF = preco * quant
    print(f"Total: R$ {precoF:.2f}") 

elif produto == 2:
    preco = 6.50
    precoF = preco * quant
    print(f"Total: R$ {precoF:.2f}") 

elif produto == 3:
    preco = 5.00
    precoF = preco * quant
    print(f"Total: R$ {precoF:.2f}") 

elif produto == 4:
    preco = 3.00
    precoF = preco * quant
    print(f"Total: R$ {precoF:.2f}")     

elif produto == 5:
    preco = 2.00
    precoF = preco * quant
    print(f"Total: R$ {precoF:.2f}")     