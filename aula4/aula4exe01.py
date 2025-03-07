preco = float(input("Indique o preço do produto origem: "))
codigo = int(input("Indique o código do produto de origem: "))
if codigo == 1:
    print(f'''Procedencia:
Sul
Preço: R${preco:.2f}''')
elif codigo == 2:
    print(f'''Procedencia:
Norte
Preço: R${preco:.2f}''')
elif codigo == 3:
    print(f'''Procedencia:
Leste
Preço: R${preco:.2f}''')  
elif codigo == 4:
    print(f'''Procedencia:
Oeste
Preço: R${preco:.2f}''')   
elif codigo == 5 or codigo == 6:
    print(f'''Procedencia:
Nordeste
Preço: R${preco:.2f}''')     
elif codigo == 7 or codigo == 8 or codigo == 9:
    print(f'''Procedencia:
Sudeste
Preço: R${preco:.2f}''')    
elif codigo >= 10 and codigo <= 20:
    print(f'''Procedencia:
Centro-Oeste
Preço: R${preco:.2f}''')    
elif codigo >= 25 and codigo <= 30:
    print(f'''Procedencia:
Nordeste
Preço: R${preco:.2f}''')
else:
     print(f'''O produto é importado!
Preço: R${preco:.2f}''')