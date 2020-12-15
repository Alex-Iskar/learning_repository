# Реализовать функцию, которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
def my_func(arg_max_1, arg_max_2, arg_long):
    for el in range(0, arg_long):
        if arg_max_1 <= list_numbers[el]:
            arg_max_1 = list_numbers[el]
        if arg_max_2 <= arg_max_1 != list_numbers[el] and arg_max_2 <= list_numbers[el]:
            arg_max_2 = list_numbers[el]
    return int(arg_max_1) + int(arg_max_2)


list_numbers = list(input("Введите три различных целых числа, с разделителем в виде пробела: ").split())
n = len(list_numbers)
max_1 = list_numbers[0]
max_2 = list_numbers[1]
print(my_func(max_1, max_2, n))
