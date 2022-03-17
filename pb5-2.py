with open("text52.txt") as f_obj2:
    cont = f_obj2.readlines()
    print('количество строк :', len(cont))
    list_of_lists = []
    for line in cont:
        line = line.split()
        list_of_lists.append(line)
    for i in range(len(list_of_lists)):
        print(f'Кол-во слов в {i+1} строке: {len(list_of_lists[i])}')
        print(list_of_lists)