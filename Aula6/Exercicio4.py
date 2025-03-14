t = int(input("aaaa"))

for linha in range(t):
    for coluna in range(t):
        if coluna >=linha:
            print(" @ ", end='')
        else:
            print(" # ", end='')    
    print()        