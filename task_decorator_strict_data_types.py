from inspect import signature
from functools import wraps
import os



def strict_argument_types(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        for i, j in enumerate(sig.parameters):
            if sig.parameters[j].annotation is not type(args[i]):
                a = str(sig.parameters[j].annotation)
                b = str(type(args[i]))
                mes = 'The argument "{}" must be "{}", passed "{}"'.format(j, a[8:-2], b[8:-2])
                raise TypeError(mes)

        return func(*args, **kwargs)
    return wrapper



def strict_return_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        result = func(*args, **kwargs)
        if isinstance(result, tuple):
            for i, j in enumerate(sig.return_annotation):
                if j is not type(result[i]):
                    a = str(j)
                    b = str(type(result[i]))
                    mes = 'The return value must be "{}", not "{}"'.format(a[8:-2], b[8:-2])
                    raise TypeError(mes)
        else:
            if sig.return_annotation is not type(result):
                a = str(sig.return_annotation)
                b = str(type(result))
                mes = 'The return value must be "{}", not "{}"'.format(a[8:-2], b[8:-2])
                raise TypeError(mes)

        return result
    return wrapper





if __name__ == '__main__':

    @strict_argument_types
    @strict_return_type
    def summa(a:int, b:int) -> int:
        return str(a + b)

    @strict_argument_types
    @strict_return_type
    def splitext(path:str) -> (str):
        filename, ext = os.path.splitext(path)
        return 1



    try:
         print(summa(1, 2))

    except TypeError as err:
        print(err)

    try:
         print(splitext("/home/usr.txt"))

    except TypeError as err:
        print(err)


