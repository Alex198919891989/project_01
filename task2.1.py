cvartals = {'Первый квартал': (1, 2, 3),
           'Второй квартал': (4, 5, 6),
           'Третий квартал': (7, 8, 9),
           'Четвертый квартал': (10, 11, 12)}
 
month = int(input('введите месяц: '))
for key in cvartals.keys():
    if month in cvartals[key]:
        print(key)