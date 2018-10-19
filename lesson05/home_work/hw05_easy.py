import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('=== 1 ===')

def make_dirs():
  for i in range(1, 10):
    name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), name)
    try:
      os.mkdir(dir_path)
    except FileExistsError:
      pass

def remove_dirs():
  for i in range(1, 10):
    name = 'dir_' + str(i)
    dir_path = os.path.join(os.getcwd(), name)
    try:
      os.rmdir(dir_path)
    except FileNotFoundError:
      pass

make_dirs()
remove_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\n=== 2 ===')
print(list(filter(os.path.isdir, os.listdir())))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\n=== 3 ===')
shutil.copyfile(sys.argv[0], 'copy of ' + os.path.basename(sys.argv[0]))
