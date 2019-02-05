print('Прудников В.В.\n')


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


class People:
    def __init__(self, surname, name, father_name):
        self._surname = surname
        self._name = name
        self._father_name = father_name

    @property
    def get_full_name(self):
        return '{} {} {}'.format(self._surname, self._name, self._father_name)

    @property
    def get_short_name(self):
        return '{} {}.{}.'.format(self._surname, self._name[:1], self._father_name[:1])

class Student(People):
    def __init__(self, surname, name, father_name, class_room, father, mather):
        People.__init__(self, surname, name, father_name)
        self._class_room = class_room
        self._parents = {'Папа': father, 'Мама': mather}

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents

class Teacher(People):
    def __init__(self, surname, name, father_name, courses, classes):
        People.__init__(self, surname, name, father_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes

class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in self._teachers if person.get_class_room in teachers.get_classes]
                lessons = [teachers.get_courses for teachers in self._teachers if person.get_class_room in teachers.get_classes]
                parents = person.get_parents

                return {'ФИО': student_full_name, 'Класс': person.get_class_room, 'Учителя': teachers, 'Предметы': lessons, 'Родитель': parents}

    @property
    def name(self):
        return self._school_name

    @property
    def adress(self):
        return self._school_adress




teachers_list = list()
teachers_list.append(Teacher('Ленин', 'Владимир', 'Ильич', 'Политология', ['9А', '9Б']))
teachers_list.append(Teacher('Юмашев', 'Иван', 'Степанович', 'Спецподготовка', ['10А', '10Б', '11А', '11Б']))
teachers_list.append(Teacher('Лаврентьева', 'Дарья', 'Михайлова', 'Первая помощь', ['9А', '9Б']))
teachers_list.append(Teacher('Нахимов', 'Павел', 'Степанович', 'Навигация', ['9А', '9Б', '10А', '10Б']))
teachers_list.append(Teacher('Лазарев', 'Михаил', 'Петрович', 'Тактика и стратегия', ['9А', '9Б', '10А', '10Б', '11А', '11Б']))
teachers_list.append(Teacher('Суворов', 'Александр', 'Васильевич', 'Личная подготовка', ['9А', '9Б', '10А', '10Б']))
teachers_list.append(Teacher('Ушаков', 'Федор', 'Федорович', 'Формации на море', ['9А', '9Б', '10А', '10Б']))
teachers_list.append(Teacher('Остряков', 'Николай', 'Алексеевич', 'Управление воздушным судном', ['10А', '10Б', '11А', '11Б']))

students_list = list()
students_list.append(Student('Сердий', 'Константин', 'Михайлович', '9А', 'Сердий М. К.', 'Сердий Р. Ш.'))
students_list.append(Student('Нор', 'Александр', 'Сергеевич', '9А', 'Нор С. Е.', 'Нор П. М.'))
students_list.append(Student('Нор', 'Артем', 'Сергеевич', '9А', 'Нор С. В.', 'Нор Е. И.'))
students_list.append(Student('Белинский', 'Лев', 'Борисович', '10А', 'Белинский Б. П.', 'Белинская Н. О.'))
students_list.append(Student('Морозова', 'Александра', 'Владимировна', '9А', 'Морозов В. Е.', 'Морозовa Г. М.'))
students_list.append(Student('Кузнецов', 'Ярослав', 'Александрович', '11Б', 'Кузнецов А. Г.', 'Кузнецовa У. П.'))
students_list.append(Student('Юрин', 'Денис', 'Александрович', '10Б', 'Юрин А. Г.', 'Юринa П. К.'))
students_list.append(Student('Крюков', 'Анатолий', 'Денисович', '11А', 'Крюков Д. Н.', 'Крюковa Е. Т.'))
students_list.append(Student('Загребельная', 'Виктория', 'Григорьевна', '9А', 'Загребельный Г. Т.', 'Загребельная Р. Р.'))
students_list.append(Student('Полегкий', 'Анатолий', 'Васильевич', '10А', 'Полегкий В. П.', 'Полегкая К. П.'))
students_list.append(Student('Мягкий', 'Филипп', 'Данилович', '11А', 'Мягкий Д. К.', 'Мягкая И. А.'))
students_list.append(Student('Прудникова', 'Алена', 'Владимировна', '11А', 'Прудников В. В.', 'Прудникова М. Е.'))
students_list.append(Student('Яровой', 'Олег', 'Сергеевич', '9А', 'Яровой С. Г.', 'Яровая К. Н.'))
students_list.append(Student('Серегина', 'Мариана', 'Ивановна', '11А', 'Серегин И. Ш.', 'Серегина П. Т.'))
students_list.append(Student('Серегин', 'Владимир', 'Владимирович', '10Б', 'Серегин В. К.', 'Серегина И. К.'))
students_list.append(Student('Королев', 'Александр', 'Степанович', '11А', 'Королев С. М.', 'Королевa Т. Е.'))
students_list.append(Student('Харченко', 'Елена', 'Генадьевна', '9Б', 'Харченко Г. К.', 'Харченко И. П.'))
students_list.append(Student('Силезнева', 'Евгения', 'Петровна', '9А', 'Силезнев П. Р.', 'Силезнева М. Р.'))



school = School('СОШ №15', 'г. Севастополь, ул. Героев Сталинграда, д. 3', teachers_list, students_list)

print(school.name)
print(school.adress)


print('\n1. Список классов школы:')
print(', '.join(school.get_all_classes()))


print('\n2. Список 9А класса:')
print('\n'.join(school.get_students('9А')))


student = school.find_student('Сердий Константин Михайлович')
print('\n3. Ученик: {}\nУчебный класс: "{}"\nУчителя: {}\nПредметы: {}'.format(student['ФИО'], student['Класс'],student['Учителя'],student['Предметы']))


print('4. Родители: {}, {}'.format(student['Родитель']['Папа'], student['Родитель']['Мама']))


print('\n5. Класс: 11А\nПреподаватели: '
      '{}'.format(', '.join(school.get_teachers('11А'))))
