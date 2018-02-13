import hashlib

valid = []

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()


def save_hash(username, password):
    with open('token.txt', 'w') as f:
        f.write(make_token(username, password))


def get_pass_from_file():
    with open('token.txt') as f:
        hesh = f.read().strip()
    return hesh


def login_required(func):
    def wrapper(*args, **kwargs):
        # get pass from file
        hesh = get_pass_from_file()
        # count attempts
        counter = 3
        # ask password and check + count
        while not valid and counter:
            usr, pswd = input(), input()
            if hesh != make_token(usr, pswd):
                counter -= 1
            else:
                valid.append(1)
        # while if not pass try again -> return none
        return func(*args, **kwargs) if valid else None
    return wrapper





@login_required
def f1():
    print('Функция защищена паролем')


@login_required
def f2():
    print('Эта функция тоже защищена паролем')


f1()
f2()
f1()

if __name__ == '__main__':
    save_hash('shaitan', '666')