my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# my_list1 = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i] and i > 0 ]
my_list1 = [el for i in range(len(my_list)) and for el in my_list if my_list[i - 1] < my_list[i] and i > 0 ]
print(f'исходный список: {my_list}')
print(f'результат: {my_list1}')