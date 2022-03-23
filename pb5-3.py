with open("text53.txt", "r") as f_obj3:
    sal = []
    emp = []
    cont = f_obj3.readlines()
    list_of_emp = []
    for line in cont:
        line = line.split()
        list_of_emp.append(line)
    for i in list_of_emp:
        sal.append(float(i[1]))
        if float(i[1]) < 20000:
            emp.append(i)
            print(i[0])
    print('Средняя зп: ', sum(sal)/len(sal))