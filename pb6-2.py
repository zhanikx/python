class Road:

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width
    def get_total_mass (self, depth, sq_mass):
        total_mass = self._width * self._lenght * sq_mass * depth
        return total_mass
a = Road(100, 15)
print(f'Масса необходимого кол-ва асфальта: {a.get_total_mass(5,25)/1000} тонн')