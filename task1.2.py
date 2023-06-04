# Задача 2
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# пункт А
x=random.choice(my_favorite_songs)
print(x)
y=random.choice(my_favorite_songs)
print(y)
z=random.choice(my_favorite_songs)
print(z)
print ('Три песни звучат', int (x[1]//1 + y[1]//1 + z[1]//1) , 'минут')
# Пункт В.
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут
from random import randint
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
i=0
c=0
while i<3:
    data = list (my_favorite_songs_dict.items())
    a, b = data [randint(0, len(data)-1)]
    print (b//1)
    c=c+b//1
    i=i+1
print ('Три песни звучат',int(c) , 'минут')