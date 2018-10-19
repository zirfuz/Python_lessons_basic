# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))
    except:
        print('не получилось создать директорию {}'.format(name))


def copy():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if not name2:
        print("Необходимо указать имя второго файла третьим параметром")
        return
    file = os.path.join(os.getcwd(), name)
    file2 = os.path.join(os.getcwd(), name2)
    try:
        shutil.copyfile(file, file2)
        print('Файл {} скопирован ({})'.format(file, file2))
    except IOError:
        print('Ошибка копирования файла {}'.format(file))


def remove():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file = os.path.join(os.getcwd(), name)
    try:
        sure = input("Вы уверены (yes/no)? ")
        if sure != 'yes':
            print('Файл {} не удалён'.format(file))
            return
        os.remove(file)
        print('Файл {} удалён'.format(file))
    except FileNotFoundError:
        print('Файл {} не найден'.format(file))


def ch_dir():
    if not name:
        print("Необходимо указать путь вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.chdir(dir_path)
        print('Текущая директория изменена на {}'.format(dir_path))
    except OSError:
        print('Ошибка изменения текущей директории {}'.format(dir_path))


def cur_dir():
    print("Текущая директория: {}".format(os.path.abspath(os.path.curdir)))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy,
    "rm": remove,
    "cd": ch_dir,
    "ls": cur_dir,
    "ping": ping
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    name2 = sys.argv[3]
except IndexError:
    name2 = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
