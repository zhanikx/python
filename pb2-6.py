n = int(input('Введите количество товаров '))
my_list = []
my_cort = ()
my_dict = dict()
analys = []
a = list()
b = list()
c = list()
d = list()
for i in range(1, n + 1):
    my_cort = list(my_cort)
    my_dict = {'Название' : input('Введи название '), 'Цена' : input('Введите цену '), 'количество' : input('Введите количество '), 'ед' : input('ед ')}
    my_cort.append(i)
    my_cort.append(my_dict)
    my_cort = tuple(my_cort)
    my_list.append(my_cort)
    a.append(my_dict.get('Название'))
    b.append(my_dict.get('Цена'))
    c.append(my_dict.get('количество'))
    d.append(my_dict.get('ед'))
    analys = dict({'Название' : a, 'Цена' : b, 'количество' : c, 'ед' : d})

print(f"Полный список: \n {my_list} \n Анализ по товарам: \n {analys}")