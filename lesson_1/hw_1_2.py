# Перевод времени в часы, минуты и секунды и вывод в формате чч:мм:сс
time = int(input("Введите количество секунд: "))
ss = time % 60
mm = (time / 60) % 60
hh = (time / 3600)
if time > 359999:
    print("Ошибка! Указанное количество секунд превышает ограничения допустимого формата отображения времени!")
elif hh < 10 and mm < 10 and ss < 10:
    print("0%d : 0%d : 0%d" % (hh, mm, ss))
elif hh < 10 and mm < 10 <= ss:
    print("0%d : 0%d : %d" % (hh, mm % 60, ss % 60))
elif hh < 10 and mm >= 10 > ss:
    print("0%d : %d : 0%d" % (hh, mm % 60, time % 60))
elif hh < 10 <= mm and ss >= 10:
    print("0%d : %d : %d" % (hh, mm % 60, time % 60))
elif hh >= 10 > mm and ss < 10:
    print("%d : 0%d : 0%d" % (hh, mm % 60, time % 60))
elif hh >= 10 > mm and ss >= 10:
    print("%d : 0%d : %d" % (hh, mm % 60, time % 60))
elif hh >= 10 and mm >= 10 > ss:
    print("%d : %d : 0%d" % (hh, mm % 60, time % 60))
elif hh >= 10 and mm >= 10 and ss >= 10:
    print("%d : %d : %d" % (hh, mm % 60, time % 60))
