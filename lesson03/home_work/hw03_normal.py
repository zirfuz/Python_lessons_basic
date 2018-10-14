# -*- coding: utf-8 -*-

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print("=== 1 ===")

def fibonacci(n, m):
  a, b = 1, 1
  ret = []
  for i in xrange(1, m + 1):
    if i >= n:
      ret.append(a)
    a, b = b, a + b
  return ret

print(fibonacci(1, 10))
print(fibonacci(2, 10))
print(fibonacci(3, 10))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print("\n=== 2 ===")

def sort_to_max(origin_list):
  for i in xrange(len(origin_list)):
    for j in xrange(i + 1, len(origin_list)):
      if origin_list[i] > origin_list[j]:
        origin_list[i], origin_list[j] = origin_list[j], origin_list[i]
  return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("\n=== 3 ===")

def my_filter(func, sequence):
  ret = []
  for x in sequence:
    if func(x):
      ret.append(x)
  return ret

print(filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14]))
print(my_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

print("\n=== 4 ===")

def diff(a, b):
  return (a[0] - b[0], a[1] - b[1])

def isParal(a1, a2, a3, a4):
  points = [a1, a2, a3, a4] # Check duplicates
  if len(points) != len(set(points)):
    return False

  diffs = []
  for b1 in points:
    for b2 in points:
      if b1 != b2:
        diffs.append(diff(b1, b2))

  hasNoPair = 0
  for df in diffs:
    if diffs.count(df) != 2:
      hasNoPair += 1
  return hasNoPair == 4

print( isParal((0, 0), (4, 0), (1, 3), (5, 3)) )
print( isParal((0, 0), (4, 0), (1, 3), (5, 4)) )
print( isParal((0, 0), (0, 1), (1, 1), (1, 0)) )
