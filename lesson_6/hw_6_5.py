# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка).
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

    def __call__(self, *args, **kwargs):
        self.draw()


class Pen(Stationery):

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


pen_p = Pen("Ручкой")
pen_p()
pencil_p = Pencil("Карандашем")
pencil_p()
handle_p = Handle("Маркером")
handle_p()
