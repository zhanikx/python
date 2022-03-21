class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'ФИО сотрудника - {self.name} {self.surname}'
    def get_total_income(self):
        return f'доход сотрудника с учетом премии - {self._income["wage"] + self._income["bonus"]}'

emp = Position('Антон','Антонов','HR', 300000, 10000)
print(emp.get_full_name())
print(emp.get_total_income())