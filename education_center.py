from abc import ABCMeta

class BaseCommunity(object):

    def __init__(self, name, teacher):
        self.__name = name
        self.__teacher = teacher
        self.__students = {}


    def append_student(self, student):
        self.__students[student.get_full_name()] = student


    def define_teacher(self, teacher):
        self.__teacher = teacher


    def pop_student(self, student):
        return self.__students.pop(student.get_full_name()[, None])


class Group(BaseCommunity):
    def __init__(self, name, teacher=None):
        super().__init__(name, teacher)


class Course(BaseCommunity):
    def __init__(self, name, teacher=None):
        super().__init__(name, teacher)












class Man():

    def __init__(self, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name


    def get_full_name(self):
        return "{} {}".format(self.__first_name, self.__second_name)





