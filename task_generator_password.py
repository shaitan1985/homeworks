import string
import random

chars = string.ascii_letters

def password_generator(lenght):
    while True:
        yield ''.join([random.choice(chars) for i in range(lenght)])





