# Вывести каждое слово с новой строки
text = input("Введите текст (в качестве разделителя допустимо использовать только пробелы): ")
norm_text = text.split()
for ind, words in enumerate(norm_text, 1):
    print(ind, words[:10:1])
