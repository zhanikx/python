def my_func(a,b,c):
    res = a + b + c - min(a,b,c)
    return res
a = int(input('первое число: '))
b = int(input('второе число: '))
c = int(input('третье число: '))
print(my_func(a,b,c))
