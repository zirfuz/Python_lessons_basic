import os
from hw05_easy import make_dir, remove_dir, print_cur_dir

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

while True:
  print('---------------------------------------\n' +
        '1. Перейти в папку\n' +
        '2. Просмотреть содержимое текущей папки\n' +
        '3. Удалить папку\n' +
        '4. Создать папку\n' +
        '---------------------------------------')

  try:
    sel = int(input('Input: '))
    if sel < 1 or sel > 4:
      raise RuntimeError()
  except:
    print('Bad input!\n')
    continue

  if sel == 1:
    fol = input('chdir: ')
    try:
      os.chdir(fol)
      print('Успешно перешел')
    except:
      print('Невозможно перейти')

  elif sel == 2:
    print_cur_dir()

  elif sel == 3:
    fol = input('Folder name: ')
    try:
      remove_dir(fol)
      print('Успешно удалено')
    except:
      print('Невозможно удалить')

  elif sel == 4:
    fol = input('Folder name: ')
    try:
      make_dir(fol)
      print('Успешно создано')
    except:
      print('Невозможно создать')

  print()
