with open("text55.txt", 'r+') as f_obj5:
    try:
        s = input('Введите числа: ')
        ss = s.split(' ')
        sss = []
        for i in range(len(ss)):
            sss.append(float(ss[i]))
        print(sum(sss))
        f_obj5.write(s)
    except ValueError:
        print('Ошибка ввода')