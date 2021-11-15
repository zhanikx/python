a = int(input("Введите результат за первый день "))
b = int(input("Введите общий результат  "))
day = 1
s = a
while s < b:
        a = a + 0.1 * a
        day += 1
        s = s + a
        print (f"Результат за {day} день {s} км")
print(f"Номер дня %.d" % day)