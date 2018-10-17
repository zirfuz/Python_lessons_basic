# Все задачи текущего блока решите с помощью генераторов списков!

import random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('=== 1 ===')

lst = [random.randint(1, 5) for _ in range(4)]
lst2 = [v ** 2 for v in lst]
print(lst)
print(lst2)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\n=== 2 ===')

fruits1 = ['apple', 'banana', 'orange', 'kiwi']
fruits2 = ['apple', 'Mango', 'banana', 'orange', 'cherry']
result = [fruit for fruit in fruits1 if fruit in fruits2]

print(fruits1)
print(fruits2)
print(result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\n=== 3 ===')

lst = [random.randint(1, 100) for _ in range(20)]
result = [value for value in lst if value % 3 == 0 and value > 0 and value % 4 != 0]

print(lst)
print(result)
