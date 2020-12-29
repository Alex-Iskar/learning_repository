# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет строк и слов.
n = 0
out_f = open("hw_5_2_file.txt", "r")
str_content = len(out_f.readlines())
print(f"Количество строк в документе: {str_content}")
out_f.close()
out_f = open("hw_5_2_file.txt", "r")
for n in range(str_content):
    num_str = n + 1
    sl_content = len(out_f.readline().split())
    print(f"Количество слов в строке №{num_str}: {sl_content} слов")
out_f.close()
