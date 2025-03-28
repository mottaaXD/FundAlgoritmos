temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
tempOr = sorted(temperaturas)
print(tempOr)
media = (tempOr[0] + tempOr[1] + tempOr[2]+ tempOr[3] + tempOr[4] + tempOr[5] + tempOr[6] + tempOr[7])/8
print(f"Maior: {tempOr[7]}")
print(f"Menor: {tempOr[0]}")
print(f"Média: {media}")