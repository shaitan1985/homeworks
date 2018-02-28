from abc import ABCMeta, abstractmethod
import datetime

class ValidatorException(BaseException):
    pass


class Validator(metaclass=ABCMeta):
    types = {}

    @abstractmethod
    def validate(value):
        pass

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException(
                "Validator must have a name!"
            )
        if not issubclass(klass, Validator):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(klass)
            )
        cls.types[name] = klass


    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(name)
            )

        return klass()



class EMailValidator(Validator):

    def validate(self, value):
        if value.count('@') == 1:
            return True
        return False


class DateValidator(Validator):

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


# Validator.add_type('email', EMailValidator)
# Validator.add_type('date', DateValidator)

# validator = Validator.get_instance('date')
# validator.validate('1/9/2017 12:00')
