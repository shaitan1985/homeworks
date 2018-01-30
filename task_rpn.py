def same_or_lower(i, top):
    lv1 = '*/'
    lv2 = '+-'
    if i in lv1 and top in lv1:
        return True
    elif i in lv2 and top in lv2:
        return True
    elif i in lv2 and top in lv1:
        return True
    else:
        return False


def move_stack(i, stack, outlst):

    if not stack or i == '(^':
        stack.append(i)
    else:
        if i == ')':
            temp = stack.pop()
            while temp != '(':
                outlst.append(temp + ' ')
                temp = stack.pop()

        elif same_or_lower(i, stack[len(stack) - 1]) :
            temp_i = stack.pop()
            if same_or_lower(i, stack[len(stack) - 1]):
                outlst.append(temp_i + ' ')
                temp_i = stack.pop()
            stack.append(i)

            return temp_i + ' '
        else:
            stack.append(i)

    return ''


def convert(expr):
    templst = ''.join(expr.split())
    outlst = []
    stack = []

    for i in templst:
        if i not in "*/^+-()":
            outlst.append(i + ' ')
        else:
            outlst.append(move_stack(i, stack, outlst))
    while stack:
        outlst.append(stack.pop() + ' ')

    return ''.join(outlst).strip()
