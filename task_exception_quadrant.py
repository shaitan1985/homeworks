from collections import Counter



def get_quadrant_number(x, y):
    if not x or not y:
        raise ValueError
    lst = []
    lst.extend([1, 4] if x > 0 else [2, 3])
    lst.extend([1, 2] if y > 0 else [3, 4])
    return int(Counter(lst).most_common(1)[0][0])


