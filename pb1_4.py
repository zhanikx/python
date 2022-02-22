x = int(input("Введите целое положительное число "))
maxx = x % 10
while x >= 1:
    x = x // 10
    if x % 10 > maxx:
        maxx = x % 10
    if x > 9:
        continue
    else:
        print("Самая большая цифра в числе ", maxx)
        break