# Реализовать проект расчета суммарного расхода ткани на производство одежды.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @property
    @abstractmethod
    def spend(self):
        pass

    def __add__(self, other):
        return self.spend + other.spend


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def spend(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def spend(self):
        return 2 * self.height + 0.3


t = Costume(150)
print(f'Затраты ткани на костюм {t.spend}')
f = Coat(30)
print(f'Затраты ткани на пальто {f.spend}')
sum_clothes = t + f
print(sum_clothes)
