
def all_to_dec(input_str, base):
    result = 0
    lens = len(input_str)
    ind = 0
    for char in input_str:
        i = ord(char)
        print(i, char)
        base_in_power = base ** (lens-ind-1)
        if i >= 48 and i <= 57:
            result += (i-48) * base_in_power
        elif i >= 65 and i <= 70:
            result += (i-55) * base_in_power
        elif i >= 97 and i <= 102:
            result += (i-87) *  base_in_power
        ind += 1
    return result


def dec_to_all(input_int, base):
    result = []
    while input_int:
        res = input_int % base
        res +=  55 if res > 9 else 48
        result.append(chr(res))
        input_int //= base
    result.reverse()
    return ''.join(result).lower()


def dec2bin(number): # возвращает str
    return dec_to_all(int(number), 2)


def dec2oct(number): # возвращает str
    return dec_to_all(int(number), 8)


def dec2hex(number): # возвращает str
    return dec_to_all(int(number), 16)


def bin2dec(number): # возвращает int
    return all_to_dec(str(number), 2)


def oct2dec(number): # возвращает int
    return all_to_dec(str(number), 8)


def hex2dec(number): # возвращает int
    return all_to_dec(str(number), 16)

if __name__ == '__main__':
    mynumber = '250'
    # mynumber = dec2bin(mynumber)
    # print(mynumber, type(mynumber))
    # mynumber = bin2dec(mynumber)
    # print(mynumber, type(mynumber))
    # mynumber = dec2oct(mynumber)
    # print(mynumber, type(mynumber))
    # mynumber = oct2dec(mynumber)
    # print(mynumber, type(mynumber))
    # mynumber = dec2hex(mynumber)
    # print(mynumber, type(mynumber))
    mynumber = hex2dec(mynumber)
    print(mynumber, type(mynumber))


