# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
class Road:
    _length = 5000
    _width = 20

    def __init__(self, mass_m, h):
        self.mass_m = mass_m
        self.h = h

    def running(self):
        print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна:'
              f' {(self._length * self._width * self.mass_m * self.h) / 1000} тонн')


mass_m_1 = int(input("Введите массу асфальта для покрытия 1 кв.м дороги толщиной в 1 см: "))
h_1 = int(input("Введите толщину дорожного полотна: "))
mass_road = Road(mass_m_1, h_1)
mass_road.running()
