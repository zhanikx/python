import tkinter
import PIL

a = 22
h = "Zhanat"
c = "Kazakhstan"
age = int(input("ВВедите ваш возраст: "))
name = input("Введите ваше имя: ")
coun = input("Введите вашу страну: ")
print("Hello! My name is %s. I'm %d years old. I'm from %s." %(name, age, coun))
print("Hello! My name is {1}. I'm {0} years old. I'm from {2}.".format(a, h, c))
