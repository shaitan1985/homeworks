from math import sqrt

errs = {
    'bad_full': "Не задана площадь участка",
    'bad_bed' : "Не задана площадь грядки",
    'bad_larger': "Размер грядки больше размера участка"
}



def get_sides(full_area):
    ratio = full_area[1].strip()
    a, b = map(int, ratio.split(":"))
    x = int(sqrt(full_area[0] * 100 / (a*b)))

    return x * a, x * b



def get_free_land(full_area, bed_area):
    full = full_area[0] * 100
    try:
        _ = 1 / full
        a, b = get_sides(full_area)
    except:
        raise ValueError(errs['bad_full'])

    x, y = bed_area
    if not x or not y:
        raise ValueError(errs['bad_bed'])



    if max(a, b) < max(x, y) or min(a, b) < min(x, y):
        raise ValueError(errs['bad_larger'])


    return full % (x*y)



if __name__ == '__main__':
    print(get_free_land((0, "1:1"), (15, 25)))