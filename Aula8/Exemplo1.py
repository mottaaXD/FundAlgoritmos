z = ['a', 'b', 'c', 'd', 'e']
for indice in range(len(z)):
    if z[indice] == 'd':
        print(f"Elemento encontrado no indice {indice}")
        break
else:
    print("Elemento não encontrado")