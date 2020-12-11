# Реализовать функцию, принимающую два числа и выполняющую их деление
def del_1(arg_1, arg_2):
    return arg_1 / arg_2


a = int(input("Введите число а : "))
b = int(input("Введите число b : "))
try:
    del_1(a, b)
except ZeroDivisionError as err:
    print("Error! Для параметра b использовано значение '0'. Введите корректное значение параметра!")
else:
    print(del_1(a, b))
