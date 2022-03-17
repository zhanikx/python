from sys import argv
name = argv[0]
time = float(argv[1])
sal = float(argv[2])
bonus = float(argv[3])
def salary():
    # time = float(input('введите время: '))
    # sal = float(input('введите ставку: '))
    # bonus = float(input('введите премию: '))
    result = time * sal + bonus
    return result
print(f'Ваша зарплата {salary()}')
