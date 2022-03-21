import time
def countdown(num_of_secs, color):
    while num_of_secs:
        min = num_of_secs//60
        sec = num_of_secs%60
        t = '{:02d}:{:02d}'.format(min, sec)
        print(f'{t} - {color}')
        time.sleep(1)
        num_of_secs -= 1

class TrafficLight:
    def __init__(self, colors):
        self.__colors = colors

    def  running(self):
        countdown(7, self.__colors[0])
        countdown(2, self.__colors[1])
        countdown(3, self.__colors[2])

p = TrafficLight(['red', 'yellow', 'green'])
p.running()