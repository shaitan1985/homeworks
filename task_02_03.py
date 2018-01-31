def average(lst):
    temp = float(0)
    lens = len(lst)
    for i in lst:
        temp += i
    return round(temp / lens , 3)
