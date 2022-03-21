with open('text56.txt') as f_obj6:
    cont = f_obj6.readlines()
    keys = []
    val = []
    lines = []
    con = 0
    for line in cont:
        line = line.split()
        lines.append(line)
    for i in lines:
        key = i[0][0:(len(i[0]) - 1)]
        keys.append(key)
        s = [int(s) for s in str.split(sentence) if s.isdigit()]
        print(s)
    print(lines)
    print(keys)
    print(val)
