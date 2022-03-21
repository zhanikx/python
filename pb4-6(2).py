from itertools import cycle
mylist = [1, 'asd', True, 4]
a = int(input('введите кол-во: '))
с = 0
for el in cycle(mylist):
    if с > a:
        break
    print(el)
    с += 1

