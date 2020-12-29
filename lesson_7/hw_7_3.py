# Реализовать программу работы с органическими клетками.
class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num == other.num:
            raise ValueError("Ошибка!!!")
        else:
            return Cell(self.num - other.num if self.num > other.num else other.num - self.num)

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(round(self.num / other.num))

    def make_order(self, line):
        v_str = "\n".join(["*" * line for n in range(self.num // line)])
        return f'{v_str}\n{"*" * (self.num % line)}'


cell_1 = Cell(33)
cell_2 = Cell(10)
cell_3 = Cell(13)
cell_4 = cell_1 + cell_2 + cell_3
print(cell_1.make_order(9))
print(cell_4)
