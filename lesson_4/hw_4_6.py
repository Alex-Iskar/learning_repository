# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
from sys import argv
from itertools import count
from itertools import cycle


def count_func(n_1, k_2):
    for el in count(n_1):
        if el > k_2:
            break
        else:
            print(el)


def cycle_func(n_1, k_2):
    c = 0
    for el in cycle(n_1):
        if c > k_2:
            break
        print(el)
        c += 1


file_path, n_1, k_2 = argv
print(count_func(int(n_1), int(k_2)))
print(cycle_func(n_1, int(k_2)))
