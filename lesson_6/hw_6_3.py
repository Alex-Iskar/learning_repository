# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position = Position(name="Иван",
                    surname="Иванов",
                    position="Analitics",
                    income={"wage": 1000,
                            "bonus": 500})


print(position.get_full_name())
print(position.get_total_income())
