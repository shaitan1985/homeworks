from collections import namedtuple


def return_namedtuple(*d_args):
    def decorator(func):
        def wrapper(*args, **kwargs):
            f_result = func(*args, **kwargs)
            if not isinstance(f_result, tuple):
                return f_result
            Named_tuple = namedtuple('my_named_tiple', list(d_args))
            f_result = Named_tuple(*f_result)
            return f_result
        return wrapper
    return decorator