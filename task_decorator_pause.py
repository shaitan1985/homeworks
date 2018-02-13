from time import sleep


def pause(sleep_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator
