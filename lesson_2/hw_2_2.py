# Реализовать обмен значений соседних элементов
n = 0
list_a = list(input("Введите список значений: "))
d = len(list_a)-1
for i in list_a:
    if n < d:
        list_a[n], list_a[n+1] = list_a[n+1], list_a[n]
    n += 2
print(list_a)
