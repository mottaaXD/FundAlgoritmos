# Recebe as dimensões do retângulo
n1 = int(input("Linhas: "))
n2 = int(input("Colunas: "))

# Itera sobre as linhas
for i in range(n1):
    # Caso seja a primeira ou última linha, imprime toda a linha
    if i == 0 or i == n1 - 1:
        print("*" * n2)
    else:
        # Caso contrário, imprime apenas as bordas esquerda e direita
        print("*" + " " * (n2 - 2) + "*")