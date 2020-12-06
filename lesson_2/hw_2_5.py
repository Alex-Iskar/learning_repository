# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел
list_a = [5, 4, 4, 2]
d = len(list_a)
n = 0
el_new = int(input(f"Введите натуральное число, для добавления в таблицу рейтинга ({list_a}) : "))
if el_new > list_a[n]:
    list_a.insert(n, el_new)
while n < d:
    if el_new < list_a[d-1]:
        list_a.insert(d, el_new)
        break
    d -= 1
print(list_a)
