sec = int(input("Введите кол-во секунд: "))
h = sec // 3600
m = (sec-h*3600)//60
s = sec -(h*3600+m*60)
print(f"Время {h}:{m}:{s}")
