dist = int(input("Qual a distancia que deseja percorrer em KM?"))

if dist <= 200:
    custo = 0.5 * dist
    print(f"A viagem vai custar: R${custo:.2f}")
else:
    custo = 0.45 * dist
    print(f"A viagem vai custar: R${custo:.2f}")    