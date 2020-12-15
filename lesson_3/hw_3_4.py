# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y)
def my_func_1(arg_x, arg_y):
    rez = arg_x**arg_y
    return rez


def my_func_2(arg_x, arg_y):
    rez = 1
    for step in range(abs(arg_y)):
        rez = rez * 1 / arg_x
    return rez


x = int(input("Введите действительное положительное значение переменной x: "))
y = int(input("Введите целое отрицательное значение переменной y: "))
print(my_func_1(x, y))
print(my_func_2(x, y))
