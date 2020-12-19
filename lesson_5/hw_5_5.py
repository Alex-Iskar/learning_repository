#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
with open("hw_5_5_file.txt", "w") as f_o:
    new_num = input("Введите числа с разделителем 'пробел' :")
    f_o.write(new_num)
with open("hw_5_5_file.txt", "r") as f_o:
    new_line = f_o.readline()
    sum_numb_list = map(int, new_line.split())
    print(sum(sum_numb_list))
