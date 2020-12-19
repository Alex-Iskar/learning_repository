# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
from sys import argv


def salary_func(h, mh, p):
    return (h * mh) + p


file_path, h, mh, p = argv
print(argv)
print(salary_func(int(h), int(mh), int(p)))
