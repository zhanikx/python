list1 = ['zima', 'leto', 'vesna', 'osen'] #by list
dict1 = {1 : 'zima', 2 : 'vesna', 'i' : 'leto', 4 : "osen'"}
n = int(input('введите номер месяца '))
if n in(1, 2, 12):
    print(list1[0])
    print(dict1.get(1))
elif n in(3, 4, 5):
    print(list1[2])
    print(dict1.get(2))
elif n == 6 or n == 7 or n == 8:
    print(list1[1])
    print(dict1.get('i'))
elif n == 9 or n == 10 or n == 11:
    print(list1[3])
    print(dict1.get(4))
else:
    print('error')
