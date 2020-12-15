# Сообщить к какому времени года относится месяц
month = int(input("Для определения времени года, ведите интересующий номер мясяца в году: "))
# Dict
season_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
               9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}
print("Вывод значения времени года, с использованием словаря: ", season_dict.get(month))
# List
season_list = ('Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer',
               'Autumn', 'Autumn', 'Autumn', 'Winter')
print("Вывод значения времени года, с использованием списка: ", season_list[month-1])
