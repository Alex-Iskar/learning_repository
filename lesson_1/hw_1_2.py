# Перевод времени в часы, минуты и секунды и вывод в формате чч:мм:сс
time = int(input("Введите количество секунд: "))
if time >= 36000:
    mm = time / 60
    hh = mm / 60
    print("%d : 0%d : 0%d" % (hh, mm % 60, time % 60))
elif time < 36000:
    mm = time / 60
    hh = mm / 60
    print("0%d : 0%d : 0%d" % (hh, mm % 60, time % 60))
elif time < 3600:
    mm = time / 60
    print("0%d : %d : 0%d" % (0, mm, time % 60))
elif time < 600:
    mm = time / 60
    print("0%d : 0%d : 0%d" % (0, mm, time % 60))
elif time < 60:
    print("0%d : 0%d : %d" % (0, 0, time))
elif time < 10:
    print("0%d : 0%d : 0%d" % (0, 0, time))
