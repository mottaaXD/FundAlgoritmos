def funcao(d, m, a):
    a_dois = a % 100
    if d * m == a_dois:
        print("Data magica encontrada!")
    else:
        print("Data magica nao foi encontrada!")
    return

dia = int(input("Digite o dia "))
mes = int(input("Digite o mes "))
ano = int(input("Digite o ano "))

funcao(dia, mes, ano)