def my_func(x, y):
    a = 1
    for i in range(-y):
        a *= 1/x
    return a
x = abs(int(input('введите число: ')))
y = (-1)*abs(int(input('введите степень: ')))
print(my_func(x, y))