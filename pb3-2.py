
def myinfo(name='Zhanat', surname='Kurmanov', year='27.01.1999', city='Almaty', email='asd@asd.com', number='+789456123'):
    return ' '.join([name, surname, year, city, email, number])
name = input('имя: ')
surname = input('фамилия: ')
year = input('дата рождения dd.mm.yyyy : ')
city = input('город: ')
email = input('почта: ')
number = input('номер телефона: ')
print (myinfo(name, surname, year, city, email, number))