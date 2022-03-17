from functools import reduce
def multpl(prevel, el):
    return prevel * el
print([i for i in range(100, 1001) if i % 2 == 0 ])
print(reduce(multpl, [i for i in range(100, 1001) if i % 2 == 0 ]))