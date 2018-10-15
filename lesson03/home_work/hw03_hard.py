# -*- coding: utf-8 -*-

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

print("=== 1 ===")

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def parseFrac(str):
  integer = 0
  frac = [0, 1]
  hasFrac = (str.find("/") != -1)
  spaceIndex = str.find(" ")
  hasInteger = (spaceIndex != -1) or (not hasFrac)
  integerStr = ""
  fracStr = ""
  if hasInteger and not hasFrac: integerStr = str
  if hasFrac and not hasInteger: fracStr = str
  if hasInteger and hasFrac:
    integerStr = str[0: spaceIndex]
    fracStr = str[spaceIndex + 1:]
  if hasInteger:
    integer = int(integerStr)
  if hasFrac:
    slashIndex = fracStr.find("/")
    frac = [int(fracStr[0: slashIndex]), int(fracStr[slashIndex + 1:])]
  frac[0] += integer * frac[1]
  return frac

expr = raw_input("expression: ")
minus = False

operatorIndex = expr.find(" - ")
if operatorIndex != -1:
    minus = True
else:
    operatorIndex = expr.find(" + ")

leftStr = expr[0: operatorIndex]
rightStr = expr[operatorIndex + 3:]

leftMinus = False
rightMinus = False

left = parseFrac(leftStr)
right = parseFrac(rightStr)

if minus:
  right[0] *= -1

cm = left[1] * right[1]

result = [left[0] * cm / left[1] + right[0] * cm / right[1], cm]

resultGcd = gcd(result[0], result[1])

result[0] /= resultGcd
result[1] /= resultGcd

negative = result[0] < 0

frac = [abs(result[0]), abs(result[1])]
integer = abs(result[0]) / abs(result[1])
frac[0] -= frac[1] * integer

resultStr = ""
if negative:
  resultStr += "-"
if integer != 0:
  resultStr += str(integer)
if integer and frac[0] != 0:
  resultStr += " "
if frac[0] != 0:
  resultStr += str(frac[0])
  resultStr += "/"
  resultStr += str(frac[1])

print(resultStr)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print("\n=== 2 ===")

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

print("\n=== 3 ===")
