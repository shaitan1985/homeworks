from task_rpn import convert
from operator import (
    add, # +
    sub, # -
    mul, # *
    truediv, # /
)


OPERATORS = {'^': pow, '*':mul,'/': truediv, '+': add, '-': sub}


def calc(expr):
    result = 0
    opn = convert(expr).split()
    stack = []
    for i in opn:
        if i in OPERATORS:
            b, a = stack.pop(), stack.pop()
            res = OPERATORS[i](a,b)
            stack.append(res)
        else:
            stack.append(float(i))
    return opn


if __name__ == '__main__':
    print(calc(input()))