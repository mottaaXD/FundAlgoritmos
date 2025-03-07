senha = int(input("Digite sua senha para entrar no sistema: "))
if senha == 1234:
    print("Acesso permitido.")
    adm = input("Deseja acessar a área administrativa? [S] [N]: ")
    if adm == "S":
        print("Entrando na área administrativa...")
    else:
        print("Você está na área de usuário comum.")
else:
    print("Senha incorreta! Acesso negado.") 