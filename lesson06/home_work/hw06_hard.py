# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname


class Job:
    def __init__(self, sallary, position, hour_rate):
        self.sallary = sallary
        self.position = position
        self.hour_rate = hour_rate


class Worker(Human):
    def __init__(self, str):
        name, surname, sallary, position, hour_rate = str.split()
        Human.__init__(self, name, surname)
        self.job = Job(int(sallary), position, int(hour_rate))

    def earned(self, hours):
        overtime = hours - self.job.hour_rate
        if overtime > 0:
            overtime *= 2
        over_sallary = (overtime / float(self.job.hour_rate)) * self.job.sallary
        total_sallary = self.job.sallary + over_sallary
        return total_sallary

    def earned_f(self, file_name):
        try:
            with open(file_name, 'r', encoding='UTF-8') as f:
                lines = f.readlines()
                for line in lines[1:]:
                    name, surname, hours = line.split()
                    if (name == self.name and surname == self.surname):
                        return self.earned(int(hours))
        except:
            pass
        return None


class Main:
    def __init__(self):
        self.__workers = []

    def set_workers(self, file_name):
        self.__workers = []
        with open(os.path.join(DIR, 'workers'), 'r', encoding='UTF-8') as f:
            for line in f.readlines()[1:]:
                self.__workers.append(Worker(line))

    def workers_earned(self, file_name):
        rnd = lambda earned: None if earned is None else round(earned)
        return '\n'.join('{}: {}'.format(w.get_full_name(), rnd(w.earned_f(file_name))) for w in self.__workers)


if __name__ == "__main__":
    DIR = './data'

    try:
        main = Main()
        main.set_workers(os.path.join(DIR, 'workers'))
        print(main.workers_earned(os.path.join(DIR, 'hours_of')))
    except:
        print("ERROR!")
