with open("text541.txt") as f_obj41:
    old = []
    new = []
    dic = ['Один', 'Два', 'Три','Четыре']
    con = 0
    cont = f_obj41.readlines()
    for line in cont:
        line = line.split()
        old.append(line)
    for i in old:
        new.append(dic[con] + ' - ' + i[2])
        con += 1
with open("text542.txt", 'w') as f_obj42:
    for n in range(len(new)):
        f_obj42.write(f'{new[n]}\n')
    print(old)
    print(new)
