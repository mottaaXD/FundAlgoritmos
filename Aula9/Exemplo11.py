#Maneira tradicional como laco "for"

quadrados = []
for x in range(10):
    quadrados.append(x*x)

#usando list comprehension
quadrados_comprehension = [x*x for x in range(10)]

print(quadrados)
print(quadrados_comprehension)