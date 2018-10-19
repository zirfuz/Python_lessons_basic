import os
import sys
import shutil

def make_dir(name):
  dir_path = os.path.join(os.getcwd(), name)
  os.mkdir(dir_path)

def remove_dir(name):
  dir_path = os.path.join(os.getcwd(), name)
  os.rmdir(dir_path)

def print_cur_dir():
  print(list(filter(os.path.isdir, os.listdir())))

if __name__ == '__main__':

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

  print('=== 1 ===')

  def make_dirs():
    for i in range(1, 10):
      name = 'dir_' + str(i)
      try:
        make_dir(name)
      except FileExistsError:
        pass

  def remove_dirs():
    for i in range(1, 10):
      name = 'dir_' + str(i)
      try:
        remove_dir(name)
      except FileNotFoundError:
        pass


  make_dirs()
  remove_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

  print('\n=== 2 ===')
  print_cur_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

  print('\n=== 3 ===')
  shutil.copyfile(sys.argv[0], 'copy of ' + os.path.basename(sys.argv[0]))
