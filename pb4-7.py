n = int(input('введите '))
def generator(el):
    for el in fact(n):
       yield el
g = generator(el)
print(g)

