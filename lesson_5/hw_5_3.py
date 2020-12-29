# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
sum_cost = 0
n = 0
out_f = open("hw_5_3_file.txt", "r")
str_content = len(out_f.readlines())
out_f.close()
out_f = open("hw_5_3_file.txt", "r")
print("Сотрудники с з/п менее 20000 рублей: ")
for n in range(str_content):
    sl_content = out_f.readline().split(",")
    if int(sl_content[1]) < 20000:
        c = sl_content[0]
        print(c)
    sum_cost = (sum_cost + int(sl_content[1]))
print("Средняя з/п на предприятии составляет: ", sum_cost / str_content)
out_f.close()
