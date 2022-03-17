line = input('введите данные: \n')
with open("text51.txt", "w") as f_obj1:
    while line:
        f_obj1.write(f'{line}\n')
        line = input('введите данные: \n')
        if not line:
            break
