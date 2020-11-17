import sys
from io import StringIO


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(pair):
    return get_pair_str(pair).split()[0]


def cdr(pair):
    return get_pair_str(pair).split()[1]


def get_pair_str(pair):
    old_stdout = sys.stdout
    pair_str = StringIO()
    sys.stdout = pair_str
    pair(print)
    sys.stdout = old_stdout

    return pair_str.getvalue()
