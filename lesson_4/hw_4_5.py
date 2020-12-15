# Реализовать формирование списка, используя функцию range() и возможности генератора.
from functools import reduce


def my_func_mng(el_1, el_2):
    return el_1 * el_2


new_list = [el for el in range(100, 1001, 2)]
print(reduce(my_func_mng, new_list))
