from itertools import chain

def read(fname):
    return open(fname).read()

def lines(fname):
    return read(fname).strip().split('\n')

def numbers(fname):
    return map(int, lines(fname))

def mapl(fn, lst): return list(map(fn, lst))

def flatten(arr):
    return list(chain.from_iterable(arr))

