def mydiv(a , b):
    if b == 0:
        return 'нельзя делить на ноль'
    else:
        return a / b
a = float(input('введите первое число: '))
b = float(input('введите второе число: '))
print (mydiv(a,b))