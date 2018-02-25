from abc import ABCMeta

class BaseCommunity(object):

    communities = {}

    def __init__(self, name, teacher=None):
        self.__name = name
        self.__teacher = teacher
        self.__students = {}
        BaseCommunity.reg_comm(self, name)

    @classmethod
    def reg_comm(cls, klass, name):
        cls.communities[name] = klass


    @classmethod
    def get_all_communities(cls):
        return dict(cls.communities)


    def append_student(self, student):
        first_name = student.get_full_info().get('first_name')
        second_name = student.get_full_info().get('second_name')

        self.__students['{} {}'.format(first_name, second_name)] = student


    def define_teacher(self, teacher):
        self.__teacher = teacher


    def pop_student(self, student):
        first_name = student.get_full_info().get('first_name')
        second_name = student.get_full_info().get('second_name')

        return self.__students.pop('{} {}'.format(first_name, second_name))


    def get_comm_students(self):
        return dict(self.__students)


    def get_comm_info(self):
        return {
            'name': self.__name,
            'teacher': self.__teacher
        }


class Group(BaseCommunity):
    pass


class Course(BaseCommunity):
    pass


class Man(object):

    def __init__(self, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name



    def get_full_info(self):

        return {
            'first_name': self.__first_name,
            'second_name': self.__second_name,
            }


class Student(Man):

    students = {}

    def __init__(self, first_name, second_name, group=None):
        super().__init__(first_name, second_name)
        self.__courses = []
        self.__group = group
        Student.reg_student(self,'{} {}'.format(first_name, second_name))


    def set_group(self, group):
        self.__group = group
        group.append_student(self)

    def remove_groupe(self, group):
        self.__group = None
        group.pop_student(self)


    def add_curse(self, course):
        self.__courses.append(course)
        course.append_student(self)


    def remove_course(self, course):
        self.remove(course)
        course.pop_student(self)

    def get_courses(self):
        return list(self.__course())

    def get_groupe(self):
        return self.__group

    @classmethod
    def reg_student(cls, klass, name):
        cls.students[name] = klass

    @classmethod
    def get_all_students(cls):
        return dict(cls.students)


class Teacher(Man):

    teachers = {}

    def __init__(self, first_name, second_name):
        super().__init__(first_name, second_name)
        self.__courses = []
        self.__groups = []
        Teacher.reg_teacher(self,'{} {}'.format(first_name, second_name))


    def add_curse(self, groups):
        self.__courses.append(groups)
        groups.define_teacher(self)


    def remove_groupe(self, groups):
        self.remove(groups)
        groups.pop_student(None)


    def add_curse(self, course):
        self.__courses.append(course)
        course.define_teacher(self)


    def course(self, course):
        self.remove(course)
        course.pop_student(self)

    def get_courses(self):
        return list(self.__courses)

    def get_groupes(self):
        return list(self.__groups)

    @classmethod
    def reg_teacher(cls, klass, name):
        cls.teachers[name] = klass

    @classmethod
    def get_all_teachers(cls):
        return dict(cls.teachers)


group_A1 = Group('A1')
history = Course('history')
programming = Course('Programming')
some_skills = Course('some_skills')
some_boring_things = Course('some_boring_things')

teacher1 = Teacher('Linus', 'Torvalds')
teacher2 = Teacher('Ricgard', 'Stollman')

student1 = Student('Vasya', 'Vasin')
student2 = Student('Katya', 'Katina')

print(BaseCommunity.get_all_communities())

teacher1.add_curse(programming)
teacher1.add_curse(some_skills)
teacher2.add_curse(history)
teacher2.add_curse(some_boring_things)
print('**********')
for item in teacher1.get_courses():
    print(item.get_comm_info().get('name'))
print('**********')
for item in Teacher.get_all_teachers():
    print(item)
print('**********')
for item in Student.get_all_students():
    print(item)
print('**********')
programming.append_student(student1)
programming.append_student(student2)

for item in programming.get_comm_students():
    print(item)
