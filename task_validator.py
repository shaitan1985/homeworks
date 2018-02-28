from abc import ABCMeta, abstractmethod
import datetime


class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    types = {}

    @abstractmethod
    def validate(value):
        pass


    @staticmethod
    def add_type(name, klass):

        if not name:
            raise ValidatorException(
                "Validator must have a name!"
            )
        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(klass)
            )
        Validator.types[name] = klass


    @staticmethod
    def get_instance(name):
        klass = Validator.types.get(name)
        print(Validator.types)
        if klass is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(name)
            )

        return klass()



class EMailValidator(Validator):

    # def __init__(self):
    #     Validator.add_type('datetime', self)

    def validate(self, value):
        if value.count('@') == 1:
            return True
        return False


class DateValidator(Validator):

    # def __init__(self):
    #     Validator.add_type('datetime', self)

    def validate(self, value):
        masks = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%m-%d-%Y",
            "%m-%d-%Y %H:%M",
            "%m-%d-%Y %H:%M:%S",
            "%m/%d/%Y",
            "%m/%d/%Y %H:%M",
            "%m/%d/%Y %H:%M:%S",
            ]

        for mask in masks:
            try:
                print(datetime.datetime.strptime(value, mask))
                return True
            except ValueError:
                pass
        return False


Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateValidator)


v