from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class Menu():

    def __init__(self):
        self.__commands = {}


    def add_command(self, name, klass):
        if not name:
            raise CommandException(
                'Command must have a name!'
                )
        if not issubclass(klass, Command):
            raise CommandException(
                'Class "{}" is not Command!'.format(klass)
                )

        self.__commands[name] = klass


    def execute(self, name, *args, **kwargs):
        command = self.__commands.get(name)
        if command is None:
            raise CommandException(
                'Command with name "{}" not found'.format(name)
                )
        command(*args, **kwargs).execute()


    def __iter__(self):
        self.__copy = self.__commands.copy()
        return self

    def __next__(self):
        while self.__copy:
            return self.__copy.popitem()
        raise StopIteration


class ShowCommand(Command):
    def __init__(self, task_id):
        pass

    def execute(self):
        pass


class ListCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass

menu = Menu()

menu.add_command('show', ShowCommand)
menu.add_command('list', ListCommand)
