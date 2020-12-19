# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
with open("hw_5_6_file.txt", "r", encoding='UTF-8') as f_o:
    new_line = f_o.readlines()
    for line in new_line:
        new_list1 = ''.join((i if i in "1234567890" else " ") for i in line)
        new_list2 = [int(i) for i in new_list1.split()]
        print(f"{line.split()[0]} {sum(new_list2)}")
