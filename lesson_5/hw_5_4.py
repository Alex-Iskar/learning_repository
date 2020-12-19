# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские
t = 0
trans_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
out_f1 = open("hw_5_4_1_file.txt", "r")
str_content = len(out_f1.readlines())
out_f1.close()
out_f1 = open("hw_5_4_1_file.txt", "r")
out_f2 = open("hw_5_4_2_file.txt", "w")
for t in range(str_content):
    sl_content1 = out_f1.readline().split()
    sl_content2 = out_f2.write(f'{trans_dict.get(sl_content1[0])} - {sl_content1[2]}\n')
out_f1.close()
out_f2.close()
