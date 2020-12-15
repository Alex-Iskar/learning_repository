# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
def fact(arg):
    f = 1
    for el in range(1, arg+1):
        f *= el
        yield f


x = 0
n = int(input("Введите число факториал 'n': "))
for el in fact(n):
    x += 1
    print(f'{x}! = {el}')
