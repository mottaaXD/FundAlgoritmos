def funcao(d, m, a):
    a_dois = a % 100
    if d * m == a_dois:
        return True

def funcao_seculoXX():
    for ano in range(1901, 2001):
        for mes in range(1, 13):
            for dia in range(1, 32):
                if(funcao(dia, mes, ano)):
                    print(f"{dia}/{mes}/{ano}")


funcao_seculoXX()