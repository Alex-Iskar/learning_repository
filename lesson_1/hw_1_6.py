# Определить номер дня, на который результат спортсмена составит не менее b километров
day = 1
a = int(input("Введите количество километров которые пробежал спортсмен в первый день: "))
b = int(input("Введите целевой результат пробежек спортсмена в километрах: "))
while a <= b:
    a = a + a * 0.1
    day += 1
print(f"Для достижения целевого результата спортсмену потребуется {day} дней.")
