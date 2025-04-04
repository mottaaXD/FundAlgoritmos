def media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

lista = [5, 12, 15, 8]
resultado = media(lista)
print(resultado)
