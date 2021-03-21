from re import findall
from common import read

def A(lst):
    return sum([len(set(findall('\w', group))) for group in lst.split('\n\n')])

def B(lst):
    return sum([len(set.intersection(*[set(findall('\w', g))\
            for g in group.split('\n')])) for group in lst.strip().split('\n\n')])

s1 ="""abc

a
b
c

ab
ac

a
a
a
a

b
"""

assert A(s1) == 11
assert B(s1) == 6

if __name__ == "__main__":
    print(A(read('6.txt')))
    print(B(read('6.txt')))
