PRT = {'^': 3, '*': 2,'/': 2, '+': 1, '-': 1, '(': 0 }
def same_or_lower(i, top):
    return True if PRT[i] <= PRT[top] else False


def move_stack(i, stack, outlst):

    if not stack or i == '(':
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

print(convert("(8+2*5)/(1+3*2-4)")) # "3 4 2 * 1 5 - 2 ^ / +"