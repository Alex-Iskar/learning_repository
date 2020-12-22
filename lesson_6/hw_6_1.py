# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск)
from time import sleep


class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(10)


color_list = ["Красный", "Желтый", "Зеленый"]
tl = TrafficLight(color_list)
tl.running()
