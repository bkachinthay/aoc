from itertools import chain 
from common import mapl, read

def conds(s):
    m = {}
    for c in s.strip().split('\n'):
        k, v = c.split(':')
        m[k] = mapl(lambda cn: mapl(int, cn.split('-')), v.split('or'))
    return m

def tickets(s):
    return mapl(lambda l: mapl(int, l.split(',')), s.strip().split('\n')[1:])

def parse(s):
    c, y, n = s.split('\n\n')
    return conds(c), tickets(y), tickets(n)

def check(rules, n):
    return any(l <= n <= h for l,h in rules)

def A(rules, your, near):
    return sum(filter(lambda n: not check(chain(*rules.values()), n), chain(*near)))

def B(rules, your, near):
    possible = [[[(n, rk, ni) if check(rv, n) else False for rk, rv in rules.items() if check(rv, n)] for ni, n in enumerate(nr)] for nr in near]
    possible = [p for p in possible if all([len(pa) for pa in p])]

    merge_possible = [set() for i in rules.keys()] 
    for p1 in possible:
        for qi1, q1 in enumerate(p1):
            new_q1 = set((q1k, q1c) for q1n, q1k, q1c in q1)
            merge_possible[qi1] = merge_possible[qi1].intersection(new_q1) if merge_possible[qi1] else new_q1

    possible = [list(m) for m in merge_possible]

    assigns = {}
    while possible:
        for q in possible:
            if len(q) == 1:
                field, idx = q[0]
                assigns[field] = idx
        new_possibles = []
        for q in possible:
            new_q = [(rx, ix) for rx, ix in q if rx not in assigns.keys()]
            if new_q:
                new_possibles.append(new_q)
        possible = new_possibles
    return prod([your[0][assigns[k]] for k in assigns.keys() if k.startswith('departure')])

def prod(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] * prod(arr[1:])

s1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

s2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

assert (A(*parse(s1))) == 71

if __name__ == "__main__":
    # print(A(*parse(read('16.txt'))))
    print(B(*parse(read('16.txt'))))
    # print(B(*parse(s2)))
    # print(B(*parse(s1)))
