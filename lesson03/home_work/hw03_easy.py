# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("=== 1 ===")

def my_round(number, ndigits):
  n = 10 ** ndigits
  number *= n
  number += 0.5
  number = int(number)
  number /= n
  return number

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("\n=== 2 ===")

def lucky_ticket(ticket_number):
  if len(str(ticket_number)) != 6:
    return False
  digit_list = [int(i) for i in str(ticket_number)]
  return sum(digit_list[0: 3]) == sum(digit_list[3: 6])

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
