def my_func(x, y):
    a = x**y
    return a
x = abs(int(input('введите число: ')))
y = (-1)*abs(int(input('введите степень: ')))
print(my_func(x, y))