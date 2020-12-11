# Суммирование чисел в строке
def sum_func(arg_sum):
    l_numbers_num = [int(n) for n in arg_sum]
    sum_list = sum(l_numbers_num)
    return sum_list


l_numbers_str_sum = input("Введите числа через пробел (Для завершения программы введите '0'): ").split()
print(sum_func(l_numbers_str_sum))
while l_numbers_str_sum.count('0') < 1:
    l_numbers_str_1 = (input("Введите числа через пробел (Для завершения программы введите '0'): ").split())
    l_numbers_str_sum = l_numbers_str_sum + l_numbers_str_1
    print(sum_func(l_numbers_str_sum))
