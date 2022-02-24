n = int(input('Введите кол-во элементов '))
list1 = []
for i in range(n):
    list1.append(input('Введите значение элемента '))
for i in range(len(list1)):
    if i % 2 != 0:
       list1[i], list1[i-1] = list1[i-1], list1[i]
print(list1)
