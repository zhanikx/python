list1 = [7, 5, 5, 3, 2]
n = int(input('введите натуральное число '))
coun = 0
for i in range(len(list1)):
    if list1[i] >= n:
       coun += 1
    else:
        break
list1.insert(coun, n)
print(list1)