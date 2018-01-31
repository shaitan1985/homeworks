def del_some(chars, s):
    for i in chars:
        if s.find(i):
            s = ''.join(s.split(i))
    return s

def is_palindrome(s):
    s = del_some(' !?,.\'"', str(s))
    center = len(s)//2
    first_part = s[0:center].lower()
    second_part = s[-1:-center-1:-1].lower()
    return True if first_part == second_part else False

