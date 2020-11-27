"""
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
"""
# My initial approach was
#
# def zero(*args, val=0): return args[0][1](val, args[0][0]) if args else val
# def one(*args, val=1): return args[0][1](val, args[0][0]) if args else val
# def plus(val): return val, operator.add
#
# After reading best practices solutions
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/solutions/python


def make_number(value, f=None):
    return value if not f else f(value)


def zero(f=None):
    return make_number(0, f)


def one(f=None):
    return make_number(1, f)


def two(f=None):
    return make_number(2, f)


def three(f=None):
    return make_number(3, f)


def four(f=None):
    return make_number(4, f)


def five(f=None):
    return make_number(5, f)


def six(f=None):
    return make_number(6, f)


def seven(f=None):
    return make_number(7, f)


def eight(f=None):
    return make_number(8, f)


def nine(f=None):
    return make_number(9, f)


def plus(x):
    return lambda y: x + y


def minus(x):
    return lambda y: y - x


def times(x):
    return lambda y: x * y


def divided_by(x):
    return lambda y: y // x


print(six(divided_by(two())))
