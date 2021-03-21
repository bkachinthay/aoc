from itertools import product
import re
from time import time
from common import read, mapl, flatten

def filterl(fn, arr):
    return list(filter(fn, arr))

def isInt(s):
    return re.match('^\d+$', s)

def toInt(s):
    return int(s) if isInt(s) else s.replace('"', '')

s1 = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

s2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

def parse(s):
    rules, strs = s.split('\n\n')
    rule_map = {}
    for l in rules.strip().split('\n'):
        k, r = l.split(':')
        rule_map[k] = [rs.strip() for rs in r.split('|')] if '"' not in r else r.strip().replace('"', '')
    return rule_map, strs.strip().split('\n')

def reduce_rules(m, idx):
    def _reduce(kv):
        if m[kv] in ['a', 'b']:
            return m[kv]
        else:
            return flatten([mapl(''.join, product(*[_reduce(p) for p in k.split(' ')])) for k in m[kv]])

    return _reduce(idx)

def A(s):
    m, lns = parse(s)
    possible = set(reduce_rules(m, '0'))
    print('max : ', max(len(p) for p in possible), len(possible))
    return len([l for l in lns if l in possible])

assert A(s1) == 2

def rec(cnt):
    c8, c11 = [], []
    for c in range(cnt):
        c8.append(('42 ' * (c +1)).strip())
        c11.append((('42 ' * (c +1)) + ('31 ' * (c+1))).strip())
    return { '42': 'a', '31': 'b', '8': c8, '11': c11}

def process_lns(lns, a, b,dl):
    return [''.join(['a' if l[li:li+dl] in a else 'b' for li in range(0, len(l), dl)]) for l in lns]

def B(s):
    m, lns = parse(s)
    pos42 = reduce_rules(m, '42') # a
    len42 = len(pos42[0])
    pos42 = set(pos42)
    pos31 = reduce_rules(m, '31') # b
    len31 = len(pos31[0])
    pos31 = set(pos31)
    lsts = process_lns(lns, pos42, pos31, len42)
    for i in range(39):
        ch = reduce_rules({**m, **rec(i)}, '0')
        x = [l for l in lsts if l in ch]
        print('iters m ', i, len(x))

ss2 = """42: 9 14 | 10 1
11: 42 42 31 31
8: 42 | 42 42
31: 14 17 | 1 13
9: "9"
14: "14"
10: "10"
1: "1"
17: "17"
13: "13"

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

    # '8': [ '42', '42 42' ],
    # '11': [ '42 31', '42 42 31 31' ],
    # '8': [ '42' ],
    # '11': [ '42 31' ],
    # '42': 'a',
    # '31': 'b',

if __name__ == '__main__':
    t = time()
    # print('19', A(read('19.txt')))
    print('B : ', B(read('19.txt')))
    # print('B : ', B(s2))
    print('time : ', time() - t)
