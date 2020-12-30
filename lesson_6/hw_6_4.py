# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go_car = {"moving": False}

    def move(self):
        self.go_car["moving"] = True

    def stop(self):
        self.go_car["moving"] = False

    def turn(self, direction):
        if direction.lower() not in {"left", "right"}:
            raise ValueError("Поворот указан не корректно!")
        elif direction == "left":
            self.go_car["direction"] = "Вы повернули на лево!"
        elif direction == "right":
            self.go_car["direction"] = "Вы повернули на право!"

    def show_speed(self):
        return {"speed": self.speed, "messages": []}

    def show_direction(self):
        return self.go_car["direction"]


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        speed_messages = super().show_speed()
        if speed_messages["speed"] > self.max_speed:
            speed_messages["messages"].append("Превышение скорости!")
        return speed_messages


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        speed_messages = super().show_speed()
        if speed_messages["speed"] > self.max_speed:
            speed_messages["messages"].append("Превышение скорости!")
        return speed_messages


car = TownCar(speed=150, color='black', name='bmw', is_police=False)
car.turn("right")
print(car.show_direction())
car.turn("right")
print(car.show_direction())
car.turn("left")
print(car.show_direction())
car.turn("left")
print(car.show_direction())
print(car.show_speed())
