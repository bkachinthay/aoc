from itertools import combinations
from common import numbers

def A(fname):
    for a, b in combinations(numbers(fname), 2):
        if (a + b) == 2020:
            return a * b

def B(fname):
    for a, b, c in combinations(numbers(fname), 3):
        if (a + b + c) == 2020:
            return a * b * c

if __name__ == "__main__":
    fname = '1a.txt'
    print(A(fname))
    print(B(fname))

