mylist = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
newlist = [el for el in mylist if mylist.count(el) == 1]
print('соответсвующий список: ', newlist)