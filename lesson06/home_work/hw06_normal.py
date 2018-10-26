# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Human:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.surname + ' ' + self.patronymic

class ClassRoom:
    def __init__(self, class_room):
        self.__class_room = {'class_num': int(class_room.split()[0]),
                             'class_char': class_room.split()[1]}
    def __eq__(self, other):
        return self.__class_room == other.__class_room
    def __hash__(self):
        return self.num * hash(self.char)

    @property
    def str(self):
        return "{} {}".format(self.num, self.char)

    @property
    def num(self):
        return self.__class_room['class_num']

    @property
    def char(self):
        return self.__class_room['class_char']


class Student(Human):
    def __init__(self, name, surname, patronymic, class_room, mother, father):
        Human.__init__(self, name, surname, patronymic)
        self.__class_room = ClassRoom(class_room)
        self.__mother = mother
        self.__father = father

    @property
    def class_room(self):
        return self.__class_room

    @property
    def mother(self):
        return self.__mother.get_full_name

    @property
    def father(self):
        return self.__father.get_full_name


class Teacher(Human):
    def __init__(self, name, surname, patronymic, subject):
        Human.__init__(self, name, surname, patronymic)
        self.subject = subject
        self.__class_rooms = []

    @property
    def class_rooms(self):
        return self.__class_rooms

    @class_rooms.setter
    def class_rooms(self, class_rooms):
        self.__class_rooms = class_rooms


class School:
    def __init__(self):
        self.__students = []
        self.__teachers = []
        self.__class_rooms = set()

    def add_student(self, student):
        self.__students.append(student)
        self.__class_rooms.add(student.class_room)

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)
        self.__class_rooms.union(teacher.class_rooms)

    def get_class_rooms(self):
        crs = [class_room.str for class_room in self.__class_rooms]
        crs.sort()
        return '\n'.join(crs)

    def get_students(self, class_room):
        cr = ClassRoom(class_room)
        students = [student.get_full_name() for student in self.__students if student.class_room == cr]
        students.sort()
        return '\n'.join(students)

    def get_subjects(self, student):
        subjects = []
        for teacher in self.__teachers:
            for class_room in teacher.class_rooms:
                if class_room == student.class_room:
                    subjects.append(teacher.subject)
        subjects.sort()
        return '\n'.join(subjects)

    def get_parents(self, student):
        return student.father() + '\n' + student.mother()

    def get_teachers(self, subject):
        teachers = [teacher.get_full_name() for teacher in self.__teachers if teacher.subject == subject]
        teachers.sort()
        return '\n'.join(teachers)



if __name__ == "__main__":
    try:
        school = School()


        teacher1 = Teacher('Васильев',    'Василий',   'Васильевич',    'Математика')
        teacher2 = Teacher('Александров', 'Александр', 'Александрович', 'Литература')
        teacher3 = Teacher('Ильин',       'Илья',      'Ильич',         'Математика')

        teacher1.class_rooms = { ClassRoom('1 А') }
        teacher2.class_rooms = { ClassRoom('1 А'), ClassRoom('2 Б') }


        student1 = Student('Иванов',   'Иван',    'Иванович',   '1 А', Human('Иванова',   'Валентина', 'Петровна'),   Human('Иванов',   'Иван',    'Александрович'))
        student2 = Student('Васильев', 'Василий', 'Васильевич', '1 А', Human('Васильева', 'Василиса',  'Васильевна'), Human('Васильев', 'Василий', 'Васильевич'))
        student3 = Student('Петров',   'Пётр',    'Петрович',   '2 Б', Human('Петрова',   'Валерия',   'Петровна'),   Human('Петров',   'Пётр',    'Иванович'))


        school.add_student(student1)
        school.add_student(student2)
        school.add_student(student3)

        school.add_teacher(teacher1)
        school.add_teacher(teacher2)
        school.add_teacher(teacher3)

        print('1) --- КЛАССЫ ---')
        print(school.get_class_rooms())
        print()

        class_room = '1 А'
        print('2) --- УЧЕНИКИ (Класс: {}) ---'.format(class_room))
        print(school.get_students(class_room))
        print()

        student = student2
        print('3) --- ПРЕДМЕТЫ (Ученик: {}) ---'.format(student.get_full_name()))
        print(school.get_subjects(student))
        print()

        student = student3
        print('4) --- РОДИТЕЛИ (Ученик: {}) ---'.format(student.get_full_name()))
        print(school.get_parents(student))
        print()

        subject = 'Математика'
        print('5) --- УЧИТЕЛЯ (Предмет: {}) ---'.format(subject))
        print(school.get_teachers(subject))
        print()

    except:
        print('ОШИБКА!')
