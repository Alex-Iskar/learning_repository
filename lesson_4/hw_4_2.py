# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in first_list if first_list[first_list.index(el) - 1] < el]
print(new_list[1::])
